import tornado.web
import tornado.ioloop

from urls import urls
from settings import settings

app = tornado.web.Application(urls, **settings)


if __name__ == '__main__':

	app.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
