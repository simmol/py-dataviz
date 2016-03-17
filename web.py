import tornado.ioloop
import tornado.web

from data import airports, routes
from utils import calc_dist


class MainHanler(tornado.web.RequestHandler):
    def get(self):
        data = routes.apply(calc_dist, args=(airports, ), axis=1).to_json()
#        self.render("templates/index.html", title="Visualization", data=data,)
        self.render("templates/histogram.html", title="Visualization", data=data,)


def make_app():
    return tornado.web.Application([
        (r"/", MainHanler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()
