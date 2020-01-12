#!/usr/bin/python3.6

import sys

feed_document = sys.stdin

for line_in_document in feed_document:
    (user_id, movie_id, rating, timestamp) = line_in_document.replace('\n', '').split(',')
    print(f"{movie_id}\t{rating}")
