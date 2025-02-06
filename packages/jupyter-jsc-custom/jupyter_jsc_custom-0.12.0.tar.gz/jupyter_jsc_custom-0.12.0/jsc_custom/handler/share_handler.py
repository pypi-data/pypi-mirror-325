import hashlib
import json
import random
import string
import urllib.parse

from jupyterhub.handlers import default_handlers
from jupyterhub.handlers.pages import SpawnHandler
from jupyterhub.utils import url_path_join
from tornado import web

from ..orm.share import UserOptionsShares


def generate_random_id():
    chars = string.ascii_lowercase
    all_chars = string.ascii_lowercase + string.digits

    # Start with a random lowercase letter
    result = random.choice(chars)

    # Add 31 more characters from lowercase letters and numbers
    result += "".join(random.choice(all_chars) for _ in range(31))

    return result


class ShareUserOptionsSpawnHandler(SpawnHandler):
    async def _render_form(self, for_user, server_name):
        auth_state = await for_user.get_auth_state()
        return await self.render_template(
            "home.html", for_user=for_user, auth_state=auth_state, row=server_name
        )

    @web.authenticated
    async def get(self, secret):
        user = self.current_user
        db_entry = UserOptionsShares.find_by_share_id(self.db, secret)
        if not db_entry:
            raise web.HTTPError(400, f"Unknown share id: {secret}")

        server_name = None
        for key, orm_spawner in user.orm_user.orm_spawners.items():
            if (
                orm_spawner.user_options
                and orm_spawner.user_options.get("share_id", "") == db_entry.share_id
            ):
                server_name = key
                break

        if not server_name:
            server_name = generate_random_id()

        spawner = user.get_spawner(server_name, replace_failed=True)

        spawner.user_options = db_entry.user_options
        service = db_entry.user_options.get("service", "jupyterlab")
        spawner.user_options["share_id"] = secret
        spawner.orm_spawner.user_options = db_entry.user_options
        self.db.add(spawner.orm_spawner)
        self.db.commit()

        url = url_path_join(self.hub.base_url, "home")
        self.redirect(f"{url}?service={service}&row={spawner.name}")


class R2DHandler(SpawnHandler):
    async def arguments_to_user_options(
        self, user, repotype_, repoowner_, repo_, ref_, arguments_dict_lower
    ):
        user_options = {}

        repotype = urllib.parse.unquote(repotype_)
        repoowner = urllib.parse.unquote(repoowner_)
        repo = urllib.parse.unquote(repo_)
        if ref_:
            ref = urllib.parse.unquote(ref_)
        else:
            ref = "HEAD"
        user_options["reporef"] = ref

        base_urls = {"gh": "https://github.com"}
        repotypes = {"gh": "GitHub"}
        if repotype not in repotypes.keys():
            raise web.HTTPError(
                400,
                f"Repo Type {repotype} not supported. Please use one of {repotypes.keys()}",
            )

        user_options["service"] = "jupyterlab"
        user_options["option"] = "repo2docker"

        if len(arguments_dict_lower.get("name", [])) > 0:
            user_options["name"] = arguments_dict_lower.get("name")[0].decode("utf-8")
        else:
            user_options["name"] = repo
        user_options["repotype"] = repotypes.get(repotype, "GitHub")
        base_url = base_urls.get(repotype, "https://github.com")
        user_options["repourl"] = f"{base_url}/{repoowner}/{repo}"

        # if "labpath" in self.request.arguments
        if len(arguments_dict_lower.get("labpath", [])) > 0:
            user_options["repopathtype"] = "File"
            user_options["repopath"] = arguments_dict_lower.get("labpath")[0].decode(
                "utf-8"
            )
        elif len(arguments_dict_lower.get("urlpath", [])) > 0:
            user_options["repopathtype"] = "URL"
            user_options["repopath"] = arguments_dict_lower.get("urlpath")[0].decode(
                "utf-8"
            )

        # https://jupyter-jsc-dev2.fz-juelich.de/hub/r2d/gh/FZJ-JSC/jupyter-jsc-notebooks

        # Get System
        auth_state = await user.get_auth_state()
        if len(arguments_dict_lower.get("system", [])) > 0:
            system = arguments_dict_lower.get("system")[0].decode("utf-8")
        elif len(auth_state.get("outpost_flavors", {}).keys()) > 0:
            system = list(auth_state.get("outpost_flavors", {}).keys())[0]
        else:
            system = "JSC-Cloud"
        user_options["system"] = system

        # Get Flavor
        if len(arguments_dict_lower.get("flavor", [])) > 0:
            flavor = arguments_dict_lower.get("flavor")[0].decode("utf-8")
        else:
            flavors = auth_state.get("outpost_flavors", {}).get(system, {})
            flavor = max(
                flavors,
                key=lambda k: flavors.get(k, {}).get("weight", -1),
                default="_undefined",
            )
        user_options["flavor"] = flavor

        # Check if persistent storage is required
        if len(arguments_dict_lower.get("datadir", [])) > 0:
            user_options["mountuserdata"] = arguments_dict_lower.get("datadir")[
                0
            ].decode("utf-8")
        elif "datadir" in arguments_dict_lower.keys():
            user_options["mountuserdata"] = "/home/jovyan/work"

        return user_options

    @web.authenticated
    async def get(self, repotype_, repoowner_, repo_, ref_=""):
        user = self.current_user
        arguments_dict_bytes = self.request.query_arguments
        arguments_dict_lower = {k.lower(): v for k, v in arguments_dict_bytes.items()}
        user_options = await self.arguments_to_user_options(
            user, repotype_, repoowner_, repo_, ref_, arguments_dict_lower
        )
        hash_str_full = json.dumps(user_options, sort_keys=True) + user.name
        hash_str = hashlib.sha256(hash_str_full.encode()).hexdigest()
        user_options["r2d_id"] = hash_str

        server_name = None
        for key, orm_spawner in user.orm_user.orm_spawners.items():
            if (
                orm_spawner.user_options
                and orm_spawner.user_options.get("r2d_id", "") == hash_str
            ):
                server_name = key
                break

        if not server_name:
            server_name = generate_random_id()

        spawner = user.get_spawner(server_name, replace_failed=True)
        spawner.user_options = user_options
        spawner.orm_spawner.user_options = user_options
        self.db.add(spawner.orm_spawner)
        self.db.commit()

        url = url_path_join(self.hub.base_url, "home")
        self.redirect(
            f"{url}?service={user_options.get('service', 'jupyterlab')}&row={spawner.name}&start"
        )


class R2DHandler(SpawnHandler):
    @web.authenticated
    async def get(self, repotype_, repoowner_, repo_, ref_=""):
        user = self.current_user
        arguments_dict_bytes = self.request.query_arguments
        arguments_dict_lower = {k.lower(): v for k, v in arguments_dict_bytes.items()}
        user_options = {}

        repotype = urllib.parse.unquote(repotype_)
        repoowner = urllib.parse.unquote(repoowner_)
        repo = urllib.parse.unquote(repo_)
        if ref_:
            ref = urllib.parse.unquote(ref_)
        else:
            ref = "HEAD"
        user_options["gitref"] = ref

        base_urls = {"gh": "https://github.com"}
        repotypes = {"gh": "GitHub"}
        if repotype not in repotypes.keys():
            raise web.HTTPError(
                400,
                f"Repo Type {repotype} not supported. Please use one of {repotypes.keys()}",
            )
        user_options["profile"] = "JupyterLab/repo2docker"

        if len(arguments_dict_lower.get("name", [])) > 0:
            user_options["name"] = arguments_dict_lower.get("name")[0].decode("utf-8")
        else:
            user_options["name"] = repo
        user_options["type"] = repotypes.get(repotype, "GitHub")
        base_url = base_urls.get(repotype, "https://github.com")
        user_options["repo"] = f"{base_url}/{repoowner}/{repo}"

        # if "labpath" in self.request.arguments
        if len(arguments_dict_lower.get("labpath", [])) > 0:
            user_options["notebook_type"] = "File"
            user_options["notebook"] = arguments_dict_lower.get("labpath")[0].decode(
                "utf-8"
            )
        elif len(arguments_dict_lower.get("urlpath", [])) > 0:
            user_options["notebook_type"] = "URL"
            user_options["notebook"] = arguments_dict_lower.get("urlpath")[0].decode(
                "utf-8"
            )

        # Get System
        auth_state = await user.get_auth_state()
        if len(arguments_dict_lower.get("system", [])) > 0:
            system = arguments_dict_lower.get("system")[0].decode("utf-8")
        elif len(auth_state.get("outpost_flavors", {}).keys()) > 0:
            system = list(auth_state.get("outpost_flavors", {}).keys())[0]
        else:
            system = "JSC-Cloud"
        user_options["system"] = system

        # Get Flavor
        if len(arguments_dict_lower.get("flavor", [])) > 0:
            flavor = arguments_dict_lower.get("flavor")[0].decode("utf-8")
        else:
            flavors = auth_state.get("outpost_flavors", {}).get(system, {})
            flavor = max(
                flavors,
                key=lambda k: flavors.get(k, {}).get("weight", -1),
                default="_undefined",
            )
        user_options["flavor"] = flavor

        # Check if persistent storage is required
        if len(arguments_dict_lower.get("datadir", [])) > 0:
            user_options["userdata_path"] = arguments_dict_lower.get("datadir")[
                0
            ].decode("utf-8")
        elif "datadir" in arguments_dict_lower.keys():
            user_options["userdata_path"] = "/home/jovyan/work"

        # create servername
        hash_str = json.dumps(user_options, sort_keys=True) + user.name
        server_name = hashlib.sha256(hash_str.encode()).hexdigest()[:32]
        spawner = user.get_spawner(server_name, replace_failed=True)

        pending_url = self._get_pending_url(user, server_name)

        if spawner.ready:
            self.log.info("Server %s is already running", spawner._log_name)
            next_url = self.get_next_url(user, default=user.server_url(server_name))
            self.redirect(next_url)
            return

        elif spawner.active:
            self.log.info("Server %s is already active", spawner._log_name)
            self.redirect(pending_url)
            return

        return await self._wrap_spawn_single_user(
            user, server_name, spawner, pending_url, user_options
        )


default_handlers.append((r"/share/user_options/([^/]+)", ShareUserOptionsSpawnHandler))
default_handlers.append((r"/r2d/([^/]+)/([^/]+)/([^/]+)", R2DHandler))
default_handlers.append((r"/r2d/([^/]+)/([^/]+)/([^/]+)/([^/]+)", R2DHandler))
default_handlers.append((r"/v2/([^/]+)/([^/]+)/([^/]+)", R2DHandler))
default_handlers.append((r"/v2/([^/]+)/([^/]+)/([^/]+)/([^/]+)", R2DHandler))
