
import os
import functools

import tornado.ioloop
import tornado.web

from search_handler import SearchHandler


class GlobalItem(object):
    def __init__(self):
        self.name = "tornado"


global_item = GlobalItem()


class SyncHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        os.system("ping -c 10 www.baidu.com")
        self.finish("Sync ping finished")


class AsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        print(global_item.name)
        global_item.name = "async"

        tornado.ioloop.IOLoop.instance().add_timeout(1, callback=functools.partial(self.ping, "www.baidu.com"))
        self.finish("Async ping finished")

    @tornado.gen.coroutine
    def ping(self, url):
        os.system(f"ping -c 10 {url}")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(global_item.name)
        global_item.name = "main"
        self.write("Hello, world")


class RaiseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print(global_item.name)
        global_item.name = "raise"
        raise Exception("tornado exception test")


def make_app():
    handlers = [
        (r"/", MainHandler),
        (r"/sync", SyncHandler),
        (r"/async", AsyncHandler),
        (r"/raise", RaiseHandler),
        (r"/search", SearchHandler),
    ]
    settings = {
        "debug": True
    }
    app = tornado.web.Application(
        handlers = handlers,
        settings = settings
    )

    app.global_item = global_item

    return app


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
