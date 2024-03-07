# pcost.py
#
# Exercise 1.27

import sys 

# file = "Data/portfolio.csv"

def portfolio_cost(file):
    with open(file, 'rt') as f:
        headers = next(f)
        cost = 0
        for line in f:
            data = line.split(',')
            try:
                num_shares=int(data[1])
            except ValueError:
                print(f"Missing Value in {line}", end='')
            price_shares=float(data[2])
            cost = cost + (num_shares * price_shares)
    return cost            

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
