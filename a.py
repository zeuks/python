import numpy as np
import pickle

with open('score_data.pickle','rb') as fp:
    score = pickle.load(fp)

above_90 = 0
below_50 = 0
total_sum = 0
total_length = 0
total_variance_sum = 0

for (subj,data) in score.items():
    variance_sum = 0
    sum_ = sum(data)
    length = len(data)
    total_sum += sum(data)
    total_length += len(data)
    mean = sum_/length
    for y in data:
        variance_sum += (mean-y) ** 2
    variance = variance_sum/length
    std = variance ** 0.5
    print("%s: average: %s variance: %s standard deviation: %s" % (subj, int(mean), int(variance), int(std)))
    above_90 = 0
    below_50 = 0
    for y in score[subj]:
        if y >= 90:
            above_90 += 1
        elif y <= 50:
            below_50 += 1
    print("%s: above 90: %s, below 50: %s" % (subj, above_90, below_50))

total_mean = total_sum/total_length
for x in score:
    for y in score[x]:
        total_variance_sum += (total_mean-y) ** 2
    total_variance = total_variance_sum/total_length
    total_std = total_variance ** 0.5

print("Total average: %s" % (int(total_mean)))
print("Total variance: %s" % (int(total_variance)))
print("Total standard deviation: %s" % (int(total_std)))
