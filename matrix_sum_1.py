A = [[3,4,5],[6,7,8],[1,3,4],[2,4,6]]

sum_A = 0
for row in range(4):
    for items in range(3):
        sum_A += A[row][items]

print (sum_A)
