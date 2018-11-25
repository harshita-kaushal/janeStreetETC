import strategy

class Arbitrage(strategy.Strategy):

	def __init__(self):
		strategy.Strategy.__init__()
		self.trading_options = ['BABA', 'BABZ']
		self.fair_price_total = 0
		self.timestep = 0
		self.num_stocks = [0,0]

		buy babz, sell baba
	def trade(self):

		while True:
			response_exchange = self.read_from_exchange()
			self.arbi_trade(response_exchange)

	def arbi_trade(self, response_exchange):
		if response_exchange['type'] == 'book':

			if response_exchange['symbol'] in ['BABZ']:

				max_buy_price = response_exchange['buy'][0][0]
				min_sell_price = response_exchange['sell'][0][0]
				self.fair_price += (max_buy_price + min_sell_price)/2 
				self.timestep += 1

			if response_exchange['symbol'] in self.trading_options:
				if response_exchange['symbol'] == 'BABA':
					request = 


					










