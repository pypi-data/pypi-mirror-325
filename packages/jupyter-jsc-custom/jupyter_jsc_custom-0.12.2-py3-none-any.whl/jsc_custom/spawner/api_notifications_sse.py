import asyncio
import inspect
import json

from async_generator import aclosing
from jupyterhub.apihandlers import default_handlers
from jupyterhub.apihandlers.users import APIHandler
from jupyterhub.utils import iterate_until
from jupyterhub.utils import url_escape_path
from jupyterhub.utils import url_path_join
from outpostspawner.api_flavors_update import async_get_flavors
from tornado import web
from tornado.iostream import StreamClosedError

from ..apihandler.user_count import get_user_count
from .utils import get_global_sse


class SSEAPIHandler(APIHandler):
    """EventStream handler to update the frontend if something changes on the backend"""

    keepalive_interval = 8
    waiting_for_cancel = {}
    spawner_tasks = {}

    def get_content_type(self):
        return "text/event-stream"

    async def send_event(self, event):
        try:
            self.write(f"data: {json.dumps(event)}\n\n")
            await self.flush()
        except StreamClosedError:
            self.log.warning("Stream closed while handling %s", self.request.uri)
            # raise Finish to halt the handler
            raise web.Finish()

    def initialize(self):
        self._finish_future = asyncio.Future()

    async def stop_after_n_seconds(self, n):
        await asyncio.sleep(n)
        self._finish_future.set_exception(
            asyncio.TimeoutError(f"Stopped SSE after {n} seconds.")
        )

    def on_finish(self):
        try:
            for task in list(self.spawner_tasks.values()):
                try:
                    task.cancel()
                except:
                    pass
        except:
            self.log.exception("Could not cancel tasks")
        try:
            self._finish_future.set_result(None)
        except:
            pass

    async def keepalive(self):
        """Write empty lines periodically

        to avoid being closed by intermediate proxies
        when there's a large gap between events.
        """
        while not (self._finish_future.done()):
            try:
                self.write("\n\n")
                await self.flush()
            except (StreamClosedError, RuntimeError):
                return

            await asyncio.wait([self._finish_future], timeout=self.keepalive_interval)

    async def get_global_event_data(self, user):
        event_data = {
            "usercount": get_user_count(self.db),
        }
        if user:
            event_data["flavors"] = await async_get_flavors(self.log, user)
        return event_data

    async def handle_spawner_progress(self, spawner):
        failed_event = {"progress": 100, "failed": True, "message": "Spawn failed"}

        def format_event(event):
            return {"progress": {spawner.name: event}}

        async def get_ready_event():
            url = url_path_join(spawner.user.url, url_escape_path(spawner.name), "/")
            ready_event = original_ready_event = {
                "progress": 100,
                "ready": True,
                "message": f"Server ready at {url}",
                "html_message": 'Server ready at <a href="{0}">{0}</a>'.format(url),
                "url": url,
            }
            try:
                ready_event = spawner.progress_ready_hook(spawner, ready_event)
                if inspect.isawaitable(ready_event):
                    ready_event = await ready_event
            except Exception as e:
                ready_event = original_ready_event
                self.log.exception(f"Error in ready_event hook: {e}")
            return ready_event

        if spawner.ready:
            # spawner already ready. Trigger progress-completion immediately
            self.log.info("Server %s is already started", spawner._log_name)
            ready_event = await get_ready_event()
            await self.send_event(format_event(ready_event))
            return

        spawn_future = spawner._spawn_future

        if not spawner._spawn_pending:
            # not pending, no progress to fetch
            # check if spawner has just failed
            f = spawn_future
            if f and f.done() and f.exception():
                exc = f.exception()
                message = getattr(exc, "jupyterhub_message", str(exc))
                failed_event["message"] = f"Spawn failed: {message}"
                html_message = getattr(exc, "jupyterhub_html_message", "")
                if html_message:
                    failed_event["html_message"] = html_message
                if (
                    hasattr(spawner, "_cancel_wait_event")
                    and spawner._cancel_wait_event
                ):
                    self.waiting_for_cancel[spawner.name] = asyncio.Event()
                    await spawner._cancel_wait_event.wait()
                    self.waiting_for_cancel[spawner.name].set()
                await self.send_event(format_event(failed_event))
                return

        # retrieve progress events from the Spawner
        async with aclosing(
            iterate_until(spawn_future, spawner._generate_progress())
        ) as events:
            try:
                async for event in events:
                    # don't allow events to sneakily set the 'ready' flag
                    if "ready" in event:
                        event.pop("ready", None)
                    if (
                        event.get("failed", False)
                        and hasattr(spawner, "_cancel_wait_event")
                        and spawner._cancel_wait_event
                    ):
                        self.waiting_for_cancel[spawner.name] = asyncio.Event()
                        await spawner._cancel_wait_event.wait()
                        self.waiting_for_cancel[spawner.name].set()
                    if event.get("progress", 10) != 0:
                        await self.send_event(format_event(event))
            except asyncio.CancelledError:
                pass
        await asyncio.wait([spawn_future])

        if spawner.ready:
            # spawner is ready, signal completion and redirect
            self.log.info("Server %s is ready", spawner._log_name)
            ready_event = await get_ready_event()
            await self.send_event(format_event(ready_event))
        else:
            # what happened? Maybe spawn failed?
            f = spawn_future
            if f and f.done() and f.exception():
                exc = f.exception()
                message = getattr(exc, "jupyterhub_message", str(exc))
                failed_event["message"] = f"Spawn failed: {message}"
                html_message = getattr(exc, "jupyterhub_html_message", "")
                if html_message:
                    failed_event["html_message"] = html_message
            else:
                self.log.warning(
                    "Server %s didn't start for unknown reason", spawner._log_name
                )
            if hasattr(spawner, "_cancel_wait_event") and spawner._cancel_wait_event:
                self.waiting_for_cancel[spawner.name] = asyncio.Event()
                await spawner._cancel_wait_event.wait()
                self.waiting_for_cancel[spawner.name].set()
            await self.send_event(format_event(failed_event))

    async def event_generator(self, user):
        # user_sse = None
        spawners = {}
        if user:
            # user_sse = get_user_sse(user.id)
            spawners = {
                s.name: s for s in user.spawners.values() if s.pending == "spawn"
            }

        self.spawner_tasks = {}
        global_sse = get_global_sse()

        # Start handling progress for each active spawner
        for server_name, spawner in spawners.items():
            task = asyncio.create_task(self.handle_spawner_progress(spawner))
            self.spawner_tasks[server_name] = task

        try:
            while not self._finish_future.done():
                await global_sse.wait()
                try:
                    if user:
                        # Re-evaluate the active spawners list after an update
                        new_spawners = {
                            s.name: s
                            for s in user.spawners.values()
                            if s.pending == "spawn"
                        }

                        # Cancel existing tasks that are no longer relevant (spawners that have finished)
                        for spawner_name in list(self.spawner_tasks.keys()):
                            if spawner_name not in new_spawners:
                                if self.waiting_for_cancel.get(spawner_name):
                                    await self.waiting_for_cancel[spawner_name].wait()
                                    try:
                                        self.waiting_for_cancel.pop(spawner_name)
                                    except KeyError:
                                        pass
                                try:
                                    task = self.spawner_tasks.pop(spawner_name)
                                except KeyError:
                                    pass
                                task.cancel()

                        # Start new tasks for the updated list of spawners
                        for spawner_name, spawner in new_spawners.items():
                            if spawner_name not in self.spawner_tasks:
                                task = asyncio.create_task(
                                    self.handle_spawner_progress(spawner)
                                )
                                self.spawner_tasks[spawner_name] = task

                        event = await self.get_global_event_data(user)
                        yield event
                        global_sse.clear()
                except:
                    self.log.exception("Exception in SSE Handling")

        except asyncio.CancelledError:
            # Handle the cleanup of tasks if needed
            pass

    async def event_generator_wrap(self, user):
        first_event = await self.get_global_event_data(user)
        yield first_event

        try:
            async for event in self.event_generator(user):
                yield event
        except asyncio.CancelledError:
            pass
        finally:
            pass

    # @needs_scope('read:servers')
    async def get(self, user_name=""):
        self.set_header("Cache-Control", "no-cache")
        self.set_header("X-Accel-Buffering", "no")
        self.set_header("Connection", "close")
        if user_name:
            user = self.find_user(user_name)
        else:
            user = None

        # start sending keepalive to avoid proxies closing the connection
        asyncio.ensure_future(self.stop_after_n_seconds(900))
        asyncio.ensure_future(self.keepalive())

        try:
            async with aclosing(
                iterate_until(self._finish_future, self.event_generator_wrap(user))
            ) as events:
                try:
                    async for event in events:
                        if event:
                            await self.send_event(event)
                        # Clear event after sending in case stream has been closed
                except asyncio.CancelledError:
                    pass
                except RuntimeError:
                    # Triggered by stop_after_n_seconds
                    pass
        except asyncio.TimeoutError as e:
            pass
        finally:
            self.finish()


default_handlers.append((r"/api/sse/([^/]+)", SSEAPIHandler))
default_handlers.append((r"/api/sse", SSEAPIHandler))
