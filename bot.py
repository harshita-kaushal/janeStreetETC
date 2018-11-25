#!/usr/bin/python
#Harshita-Neeraj
# ~~~~~==============   HOW TO RUN   ==============~~~~~
# 1) Configure things in CONFIGURATION section
# 2) Change permissions: chmod +x bot.py
# 3) Run in loop: while true; do ./bot.py; sleep 1; done

from __future__ import print_function

import sys
import socket
import json
import time


### TRADING STRATEGIES
import penny
import simple_bond

# ~~~~~============== CONFIGURATION  ==============~~~~~
# replace REPLACEME with your team name!
team_name="teamyellow"
# This variable dictates whether or not the bot is connecting to the prod
# or test exchange. Be careful with this switch!
test_mode = True

# This setting changes which test exchange is connected to.
# 0 is prod-like
# 1 is slower
# 2 is empty
test_exchange_index=1
prod_exchange_hostname="production"

port=25000 + (test_exchange_index if test_mode else 0)
exchange_hostname = "test-exch-" + team_name if test_mode else prod_exchange_hostname

# ~~~~~============== NETWORKING CODE ==============~~~~~
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((exchange_hostname, port))
    return s.makefile('rw', 1)

def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")

def read_from_exchange(exchange):
    return json.loads(exchange.readline())


# ~~~~~============== MAIN LOOP ==============~~~~~
    
def interpret_exchange(exchange):
    interpreter = response_from_exchange(exchange)
    if interpreter['type'] == 'book' and interpreter['symbol'] == 'bond':
        max_share_price = interpreter['buy'][0][0]


def main():
    strategy = sys.argv[1]

    exchange = connect()
    write_to_exchange(exchange, {"type": "hello", "team": team_name.upper()})
    hello_from_exchange = read_from_exchange(exchange)
    order_id = 0
    while True:
        response_exchange = read_from_exchange(exchange)
        if strategy == 'bond':
            simple_bond.bond_strategy(response_exchange)
        elif strategy == 'penny':
            penny.bond_strategy(response_exchange, team_name, order_id)

        order_id += 1
        time.sleep(2)

if __name__ == "__main__":
    main()