import json

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado

from .config import UserConfigHandler

class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({
            "data": "This is /qbraid-authentication-server/get-example endpoint!"
        }))


def setup_handlers(web_app,url_path):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, url_path, "get-example")
    qbraid_route_pattern = url_path_join(base_url, url_path, "qbraid-config")
    handlers = [
        (route_pattern, RouteHandler),
        (qbraid_route_pattern,UserConfigHandler)
    ]
    web_app.add_handlers(host_pattern, handlers)
