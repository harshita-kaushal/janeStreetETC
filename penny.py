#### PENNY TRADING STRATEGY
import random
import strategy
import time

class Penny(strategy.Strategy):


	def trade(self):

		while True:
			response_exchange = self.read_from_exchange()
			self.penny_trade(response_exchange)
			time.sleep(5)

	def penny_trade(self, exchange_response):

		if exchange_response['type'] == 'book':
			try:
				max_buy_price = exchange_response['buy'][0][0]
				min_sell_price = exchange_response['sell'][0][0]
			except:
				return None

 			for trade_item in self.trades:
				
				buy_request = {"type": "add", "order_id": self.order_id, "symbol": trade_item, "dir": "BUY", "price": max_buy_price, "size": 5}
				self.write_to_exchange(buy_request)

				sell_request = {"type": "add", "order_id": self.order_id, "symbol": trade_item, "dir": "SELL", "price": min_sell_price, "size": 5}
				self.write_to_exchange(sell_request)


		return None


class BondPenny(Penny):

	def __init__(self):
    
		Penny.__init__(self)
		self.trades = ['BOND']



