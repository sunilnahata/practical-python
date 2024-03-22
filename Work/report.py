# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            stock = {
                    "name": row[0], 
                    "shares": int(row[1]), 
                    "price": float(row[2]),
                    }
            portfolio.append(stock)
            
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    
    return prices

def make_report(price, portfolio):
    rows = []
    for stock in portfolio:
        curr_price = price[stock["name"]]
        change = curr_price - stock["price"]
        summary = (stock["name"], stock["shares"], curr_price, change)
        rows.append(summary)

    return rows


portfolio = read_portfolio('Data/portfolio.csv')
price = read_prices('Data/prices.csv')

cost = 0
for share in portfolio:
    cost += share["shares"] * share["price"]
print(f"Total cost: {cost}")

curr_val = 0
for share in portfolio:
    curr_val += share["shares"] * price[share["name"]]

print(f"Current value: {curr_val}")
print(f"Profit: {curr_val - cost}")


