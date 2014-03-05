#!/usr/bin/env python
import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import pymongo
import time
import datetime
import json
import urllib
from tornado.options import define, options

define("port",default=8000,help="Run on the given port",type=int)
class Application(tornado.web.Application):
	def __init__(self):
		handlers = [(r'/',IndexHandler)]
		tornado.web.Application.__init__(self,handlers,debug=True)
class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		query = self.get_argument('q')
		client = tornado.httpclient.HTTPClient()
		repsonse = client.fetch("http://search.twitter.com/search.json?"+ \
				urllib.urlencode({"q":query,"result_type":"recent","rpp":100}))
		body = json.loads(reponse.body)
		result_count = len(body['result'])
		now = datetime.datetime.utcnow()
		raw_oldest_tweet_at = body['result'][-1]['created_at']
		oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
				"%a, %d %b %Y %H:%M:$S +0000")
		seconds_diff = time.mktime(now.timetuple()) - \
				time.mktime(oldest_tweet_at.timetuple())
		tweets_per_second = float(result_count)/seconds_diff
		self.write("""
		<div style="text-align:center">
			<div style="font-size: 72px">%s</div>
			<div style="font-size: 144px">%.02f</div>
			<div style="font-size: 72px">tweets per second</div>
		</div>""" % (query,tweets_per_second))

	
if __name__ == "__main__":
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

