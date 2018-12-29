import tornado.web


class HomeView(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')
