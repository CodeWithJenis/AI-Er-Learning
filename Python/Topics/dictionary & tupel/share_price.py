'''You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.'''

# But best will be done through function

import statistics
stock_price = {"info": [600, 630, 620], "ril": [1430, 1490, 1567],"mtl": [234, 180, 160]}
user_input = input("Enter the following operation: \n 1) print \n 2) add\n")
if user_input == "print":
    for stock, price_list in stock_price.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg: ", round(avg, 2))
else:
    stock = input("Enter stock ticker: ")
    price = input("Enter price: ")
    price = int(price)
    if stock in stock_price.keys():
       stock_price[stock].append(price)
    else:
        stock_price[stock] = [price]
    for stock, price_list in stock_price.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg: ", round(avg, 2))
