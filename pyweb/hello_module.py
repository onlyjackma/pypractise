#!/usr/bin/env python
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port",default=8000,help="Run on the given port",type=int)

class HelloHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('hello.html')
class HelloModule(tornado.web.UIModule):
	def render(self):
		return '<h1>Hello,world!</h1>'


if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[
			(r'/',HelloHandler),
	],template_path=os.path.join(os.path.dirname(__file__),"hello"),
	ui_modules={'Hello':HelloModule},
	debug=True
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

