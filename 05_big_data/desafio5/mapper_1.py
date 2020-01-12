#!/usr/bin/python3.6

import sys

feed_document = sys.stdin

for line_in_document in feed_document:
    (movie_id, tag_id, relevance) = line_in_document.replace('\n', '').split(',')
    print(f"{tag_id}\t{relevance}")
