#!/usr/bin/python3.6

import sys

feed_mapper_output = sys.stdin
previous_counter = None
relevance_sum = 0.0
relevance_count = 0

for line_ocurrence in feed_mapper_output:
    tag_id, relevance = line_ocurrence.replace('\n', '').split('\t')

    if tag_id != previous_counter:
        if previous_counter is not None:
            relevance_mean = relevance_sum/relevance_count
            print(f"{previous_counter}\t{str(relevance_mean)}")
        previous_counter = tag_id
        relevance_sum = 0.0
        relevance_count = 0

    relevance_sum += float(relevance)
    relevance_count += 1

relevance_mean = relevance_sum/relevance_count
print(f"{previous_counter}\t{str(relevance_mean)}")
