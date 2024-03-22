# pcost.py
#
# Exercise 1.27

import csv
import sys 

# file = "Data/portfolio.csv"

def portfolio_cost(file):
    with open(file, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        cost = 0
        for row_num, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
#            data = row.split(',')
            try:
                num_shares=int(record["shares"])
            except ValueError:
                print(f"Row {row_num}: Bad row: {row}")
#                print(f"Missing Value in {line}", end='')
            price_shares=float(record["price"])
            cost += (num_shares * price_shares)
    return cost            

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
