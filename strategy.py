#!/usr/bin/env python
 
from __future__ import print_function

import sys
import socket
import json
import time

class Strategy:
	def __init__(self):

		self.team_name="teamyellow"

		# This variable dictates whether or not the bot is connecting to the prod
		# or test exchange. Be careful with this switch!

		self.test_mode = True


		# This setting changes which test exchange is connected to.
		# 0 is prod-like
		# 1 is slower
		# 2 is empty

		self.test_exchange_index=0
		self.prod_exchange_hostname="production"

		self.port=25000 + (self.test_exchange_index if self.test_mode else 0)
		self.exchange_hostname = "test-exch-" + self.team_name if self.test_mode else self.prod_exchange_hostname
		#assert self.exchange_hostname == self.prod_exchange_hostname
		#assert False
		self.exchange = self.connect()
		self.order_id = 0
		self.map = {}
		self.trades = ['AAPL', 'BABA', 'BABZ', 'BOND', 'GOOG', 'MSFT', 'XLK']
		self.initiate_trade()

	def connect(self):
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    s.connect((self.exchange_hostname, self.port))
	    return s.makefile('rw', 1)

	def write_to_exchange(self, obj):

		#print('sending an order')
		json.dump(obj, self.exchange)
		self.exchange.write("\n")
		self.map[self.order_id] = obj
		self.order_id += 1


	def read_from_exchange(self):
	    return json.loads(self.exchange.readline())

	def initiate_trade(self):
		### Initiate Trade
		self.write_to_exchange({"type": "hello", "team": self.team_name.upper()})
		hello_from_exchange = self.read_from_exchange()

	def trade(self):
		pass





