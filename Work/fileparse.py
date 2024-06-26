# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv_file(filename, **kwargs):
    '''
    This function parses a csv given a filename as input
    '''
    with open(filename) as f:
        return parse_csv(f.readlines(), **kwargs)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    '''
    This function parses a csv given an iterable as input
    '''
    if select and not has_headers:
        raise RuntimeError("Select requires column headers")
    rows = csv.reader(lines, delimiter=delimiter)
    header = next(rows) if has_headers else []
    if select:
        indices = [header.index(colname) for colname in select]
        header = select

    records = []
    for row_num, row in enumerate(rows, 1):
        if not row:
            continue
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(value) for func, value in zip(types,row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {row_num}: Couldn't convert {row}")
                    print(f"Row {row_num}: Reason {e}")
                continue
        if header:
            record = dict(zip(header, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
