#pcost.py
#calculate total cost of portfolio in portfolio.csv
#11/17/2021

import sys
#import os
#import gzip
import csv

def portfolio_cost(filename):
	f = open(filename, 'rt')
	rows = csv.reader(f)
	headers = next(rows)
	Total = 0

	for row in rows:
	#	row = line.split(',')
		print(row)
		try:
			shares = int(row[1])
			cost = float(row[2])
			Total = Total + (shares * cost)
		except ValueError:
			print("Couldn't parse", row)

	f.close()
	return Total

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost1 = portfolio_cost(filename)
print('Total cost:', cost1)