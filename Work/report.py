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
            record = dict(zip(header, row))
# Remove the following section when zipping records 
#            stock = {
#                    "name": row[0], 
#                    "shares": int(row[1]),     
#                    "price": float(row[2]),
#                    }
            portfolio.append(record)
            
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = row[0]
                price = float(row[1])
                prices[name] = price
            except IndexError:
                pass
    
    return prices

def make_report(portfolio, price):
    rows = []
    for stock in portfolio:
        curr_price = price[stock["name"]]
        change = curr_price - float(stock["price"])
        summary = (stock["name"], int(stock["shares"]), curr_price, change)
        rows.append(summary)

    return rows


portfolio = read_portfolio('Data/portfolio.csv')
#portfolio = read_portfolio(input("Enter the filename: ")) 
price = read_prices('Data/prices.csv')


report = make_report(portfolio, price)
header = ('Name', 'Shares', 'Price', 'Change')
print("%10s %10s %10s %10s" %header)
print(("-" * 10 + " ") * len(header))
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {f'${price:.2f}':>10} {change:>10.2f}")

##cost = 0
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
