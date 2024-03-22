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
    price = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                price[row[0]] = float(row[1])
            except IndexError:
                pass
    
    return price

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


report = make_report(price, portfolio)
header = ('Name', 'Shares', 'Price', 'Change')
print("%10s %10s %10s %10s" %header)
print(("-" * 10 + " ") * len(header))
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {f'${price:.2f}':>10} {change:>10.2f}")

#cost = 0
#for share in portfolio:
#    cost += share["shares"] * share["price"]
#print(f"Total cost: {cost}")
#
#curr_val = 0
#for share in portfolio:
#    curr_val += share["shares"] * price[share["name"]]
#
#print(f"Current value: {curr_val}")
#print(f"Profit: {curr_val - cost}")
#
