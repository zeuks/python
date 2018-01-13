score = []
scores = []

numb = int(input("What is the number of students: "))
subj = int(input("What is the number of subjects: "))

subject = 0

for x in range(subj):
    sub = 0
    subject += 1
    for y in range(numb):
        s = 0
        s = int(input("What is the score for subject %s:" % (int(subject))))
        scores.append(s)
        sub += s
    score.append(sub / numb)

total = 0
for n in score:
    print ("Subject %s average: %s" % (total + 1, int(score[total])))
    total += 1

print ("Total average: %s" % (int(sum(score) / len(score))))

total = 0
for x in score:
    vs = 0
    tn = total * numb
    ss = scores[(tn):(tn + numb):]
    s = sum(ss)
    slength = len(ss)
    mean = s / slength
    for y in ss:
        vs += (mean - y) ** 2
    variance = vs / slength
    std = variance ** 0.5
    print ("Subject %s variance: %s" % (total + 1, int(variance)))
    print ("Subject %s standard deviation: %s" % (total + 1, int(std)))
    total =+ 1
