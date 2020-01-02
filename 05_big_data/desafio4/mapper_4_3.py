import sys, re
from functools import reduce

feed_document = sys.stdin

for line in feed_document:
    line = re.sub(r'^\W+|\W+$', '', line)
    row = re.split(',', line)
    count_positive = reduce(lambda a,b : int(a)+int(b), row[:50])
    avg_positive = count_positive/50
    if avg_positive >= 0.60:
        print("{}\t{}".format(row[50], avg_positive))