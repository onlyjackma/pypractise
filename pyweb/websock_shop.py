#!/usr/bin/env python
import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
from uuid import uuid4
from tornado.options import define, options
define("port",default=8000,help="Run on the given port",type=int)

class ShoppingCart(object):
	totalInventory = 10
	callbacks = []
	carts = {}
	
	def register(self,callback):
		self.callbacks.append(callback)
	
	def unregister(self,callback):
		self.callbacks.remove(callback)

	def moveItemToCart(self,session):
		if session in self.carts:
			return

		self.carts[session] = True
		self.notifyCallbacks()

	def removeItemFromCart(self,session):
		if session not in self.carts:
			return
		
		del(self.carts[session])
		self.notifyCallbacks()

	def notifyCallbacks(self):
		for c in self.callbacks:
			self.callbackHelper(c)
	
	def callbackHelper(self,callback):
		callback(self.getInventoryCount())
	
	def getInventoryCount(self):
		return self.totalInventory - len(self.carts)

class DetailHandler(tornado.web.RequestHandler):
	def get(self):
		session = uuid4()
		count  = self.application.shoppingCart.getInventoryCount()
		self.render("index.html",session=session,count=count)

class CartHandler(tornado.web.RequestHandler):
	def post(self):
		action = self.get_argument('action')
		session = self.get_argument('session')

		if not session:
			self.set_status(400)
			return

		if action == 'add':
			self.application.shoppingCart.moveItemToCart(session)
		elif action == 'remove':
			self.application.shoppingCart.removeItemFromCart(session)
		else:
			self.set_status(400)

class StatusHandler(tornado.websocket.WebSocketHandler):
	def get(self):
		self.application.shoppingCart.register(self.callback)

	def on_close(self):
		self.application.shoppingCart.unregister(self.callback)

	def on_message(self,count):
		pass

	def callback(self,count):
		self.write('{"inventoryCount":"%d"}' % count)

class Application(tornado.web.Application):
	def __init__(self):
		self.shoppingCart = ShoppingCart()
		handlers = [
			(r'/',DetailHandler),
			(r'/cart',CartHandler),
			(r'/cart/status',StatusHandler)
		]
		settings = {
			'template_path':'websock_temp',
			'static_path':'websock'
		}
		debug = True
		tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = Application()
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

