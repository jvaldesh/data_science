#!/usr/bin/python3.6

import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    print(f"{len(row[2].split('|'))}\t1")
