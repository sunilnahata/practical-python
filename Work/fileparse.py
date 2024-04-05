# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        header = next(rows) if has_headers else []
        if select:
            indices = [header.index(colname) for colname in select]
            header = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:
                continue
            if select:
                row = [row[index] for index in indices]
            if types:
                row = [func(value) for func, value in zip(types,row)]
            if header:
                record = dict(zip(header, row))
            else:
                record = tuple(row)
            records.append(record)

    return records


