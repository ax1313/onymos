ticker_list = []
buy_list = []
sell_list = []

# Add wrapper functionality after completing this function
def addOrder(order_type, ticker_symbol, quantity, price):
    if len(ticker_list) < 1024:
        if ticker_symbol not in ticker_list:
            ticker_list.insert(ticker_symbol)
    
        if order_type.lower() == "buy":
            buy_list.insert(0, [ticker_symbol, quantity, price])
        elif order_type.lower() == "sell":
            sell_list.insert(0, [ticker_symbol, quantity, price])

# Return matching sell order
def matchOrder(ticker_symbol):

    curr_buys = []
    curr_sells = []

    # Check compatability
    max_buy_price = 0
    for buy in buy_list:
        if buy[0] == ticker_symbol:
            curr_buys.insert(0, [buy[1], buy[2]])
            if buy[2] > max_buy_price:
                max_buy_price = buy[2]

    min_sell_price = 1000000 # Assume stock price will not exceed this amount
    for sell in sell_list:
        if sell[0] == ticker_symbol:
            curr_sells.insert(0, [sell[1], sell[2]])
            if sell[2] < min_sell_price:
                min_sell_price = sell[2]
    
    if max_buy_price >= min_sell_price:
        

    return 0