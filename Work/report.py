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
