import time 

def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")
#BOOK BOND BUY 999:12 998:100 995:1 SELL 1001:4 1002:15 1003:100
# {"type":"book","symbol":"BOND","buy":[[999,12],[998,100],[995,1]],"sell":[[1001,4],[1002,15],[1003,100]]}
def bond_strategy(exchange_name, team_name, order_id):
    buy_request = {"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 5}
    #sell_request ={"type": "add", "order_id": order_id, "symbol": "BOND", "dir": "SELL", "price": 1001, "size": 5}
    
def main(response_to_exchange):
    trade(response_to_exchange, team_name, order_id)

