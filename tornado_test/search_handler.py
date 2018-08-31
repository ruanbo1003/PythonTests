
import tornado.web
import tornado.ioloop
import tornado.httpserver


import jieba

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        app = tornado.ioloop.IOLoop.current()
        print(dir(app))
        self.write("search trend")

        seg_names = jieba.cut_for_search("广东省广州市中信大厦")
        for s in seg_names:
            print(s)
