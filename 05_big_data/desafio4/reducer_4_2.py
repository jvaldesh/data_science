import sys

feed_mapper_output = sys.stdin
previous_counter = None
plan_count = 0
total_avg_plan = 0

for line in feed_mapper_output:
    plan, avg = line.split('\t')

    if plan != previous_counter:
        if previous_counter is not None and plan_count > 0:
            print("{:.2f}\t{}".format(total_avg_plan/plan_count, previous_counter))

        previous_counter = plan
        total_avg_plan = 0
        plan_count = 0

    total_avg_plan += float(avg)
    plan_count += 1

if plan_count > 0:
    print("{:.2f}\t{}".format(total_avg_plan/plan_count, previous_counter))