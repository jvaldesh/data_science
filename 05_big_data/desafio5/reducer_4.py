#!/usr/bin/python3.6

import sys

feed_mapper_output = sys.stdin
previous_counter = None
total_counter = 0

for line_ocurrence in feed_mapper_output:
    genres_count, occurence = line_ocurrence.replace('\n', '').split('\t')

    if genres_count != previous_counter:
        if previous_counter is not None:
            print(f"{previous_counter}\t{str(total_counter)}")
        previous_counter = genres_count
        total_counter = 0


    total_counter += int(occurence)

print(f"{previous_counter}\t{str(total_counter)}")
