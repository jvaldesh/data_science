#!/usr/bin/python3.6

import sys

feed_mapper_output = sys.stdin
previous_counter = None
rating_sum = 0.0
rating_count = 0

for line_ocurrence in feed_mapper_output:
    user_id, rating = line_ocurrence.replace('\n', '').split('\t')

    if user_id != previous_counter:
        if previous_counter is not None:
            rating_mean = rating_sum/rating_count
            print(f"{previous_counter}\t{str(rating_count)}\t{str(rating_mean)}")
        previous_counter = user_id
        rating_sum = 0.0
        rating_count = 0

    rating_sum += float(rating)
    rating_count += 1

rating_mean = rating_sum/rating_count
print(f"{previous_counter}\t{str(rating_count)}\t{str(rating_mean)}")
