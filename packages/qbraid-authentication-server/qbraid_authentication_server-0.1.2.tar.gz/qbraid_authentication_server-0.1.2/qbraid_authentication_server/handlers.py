from jupyter_server.utils import url_path_join

from .config import UserConfigHandler


def setup_handlers(web_app, url_path):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    qbraid_route_pattern = url_path_join(base_url, url_path, "qbraid-config")
    handlers = [(qbraid_route_pattern, UserConfigHandler)]
    web_app.add_handlers(host_pattern, handlers)
