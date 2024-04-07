# pcost.py
#
# Exercise 1.27

import report 
import sys

# file = "Data/portfolio.csv"

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([s.cost() for s in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    main(sys.argv)






























