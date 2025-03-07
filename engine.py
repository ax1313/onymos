import random

ticker_list = []
buy_list = []
sell_list = []

def addOrder(order_type, ticker_symbol, quantity, price):
    if len(ticker_list) < 1024:
        if ticker_symbol not in ticker_list:
            ticker_list.insert(ticker_symbol)
    
        if order_type.lower() == "buy":
            buy_list.insert(0, [ticker_symbol, quantity, price])
        elif order_type.lower() == "sell":
            sell_list.insert(0, [ticker_symbol, quantity, price])

# Wrapper function to randomly add buy orders for a certain ticker
def wrapper_buy(ticker_symbol):
    curr_buy_quantity = random.randint(1, 10) * 100
    curr_buy_price = random.randint(1, 200)
    addOrder("buy", ticker_symbol, curr_buy_quantity, curr_buy_price)

# Wrapper function to randomly add sell orders for a certain ticker
def wrapper_sell(ticker_symbol):
    curr_sell_quantity = random.randint(1, 10) * 100
    curr_sell_price = random.randint(1, 200)
    addOrder("sell", ticker_symbol, curr_sell_quantity, curr_sell_price)

# Return matching sell order
def matchOrder(ticker_symbol):

    curr_buys = []
    curr_sells = []

    # Check compatibility before matching
    max_buy_price = 0
    sum_buy_quantity = 0
    for buy in buy_list:
        if buy[0] == ticker_symbol:
            curr_buys.insert(0, [buy[1], buy[2]])
            sum_buy_quantity += buy[1]
            if buy[2] > max_buy_price:
                max_buy_price = buy[2]

    min_sell_price = 1000000 # Assume stock price will not exceed this amount
    for sell in sell_list:
        if sell[0] == ticker_symbol:
            curr_sells.insert(0, [sell[1], sell[2]])
            if sell[2] < min_sell_price:
                min_sell_price = sell[2]
    
    if max_buy_price >= min_sell_price:
        sum_sell_quantity = 0
        sell_ret_list = []
        for sell in curr_sells:
            if sum_sell_quantity < sum_buy_quantity:
                sum_sell_quantity += sell[1]
                sell_ret_list.append(sell)
            else:
                break
        return sell_ret_list
    else:
        return []