# report.py
#
# Exercise 2.4

import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float]) 

def read_prices(filename):
    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        curr_price = prices[stock["name"]]
        change = curr_price - float(stock["price"])
        summary = (stock["name"], int(stock["shares"]), curr_price, change)
        rows.append(summary)

    return rows


def print_report(report):
    header = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" %header)
    print(("-" * 10 + " ") * len(header))
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {f'${price:.2f}':>10} {change:>10.2f}")


def portfolio_report(portfoliofile, pricefile):
    portfolio = read_portfolio(portfoliofile)
    #portfolio = read_portfolio(input("Enter the filename: ")) 
    prices = read_prices(pricefile)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfoliodate.csv', 'Data/prices.csv')
