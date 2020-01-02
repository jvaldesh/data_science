import sys, re

feed_document = sys.stdin

for line in feed_document:
    line = re.sub(r'^\W+|\W+$', '', line)
    row = re.split(',', line)
    print(row[50] + '\t' + "1")