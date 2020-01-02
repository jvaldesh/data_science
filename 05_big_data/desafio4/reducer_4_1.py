import sys

feed_mapper_output = sys.stdin
previous_counter = None
total_word_count = 0

for line_ocurrence in feed_mapper_output:
    word, ocurrence = line_ocurrence.split('\t')

    if word != previous_counter:
        if previous_counter is not None:
            print(str(total_word_count) + '\t' + previous_counter)

        previous_counter = word
        total_word_count = 0

    total_word_count += int(ocurrence)

print(str(total_word_count) + '\t' + previous_counter)