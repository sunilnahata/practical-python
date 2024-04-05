# pcost.py
#
# Exercise 1.27

import report 
import sys

# file = "Data/portfolio.csv"

def portfolio_cost(file):
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename: ") 

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
