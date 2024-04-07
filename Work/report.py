# report.py
#
# Exercise 2.4

import fileparse
from stock import Stock

def read_portfolio(filename):
    with open(filename) as line:
        portfolio_dicts = fileparse.parse_csv(line, select=['name', 'shares', 'price'], types=[str, int, float])
    
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portfolio_dicts]
    return portfolio

def read_prices(filename):
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines,types=[str,float], has_headers=False))

def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        curr_price = prices[stock.name]
        change = curr_price - stock.price
        summary = (stock.name, stock.shares, curr_price, change)
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


def main(args):
    if len(args) != 3:
        raise SystemExit("Usage: %s portfoliofile pricefile" % args[0])
    portfolio_report(args[1], args[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
