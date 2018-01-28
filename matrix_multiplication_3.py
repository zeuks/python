import numpy as np

a_col, a_row = [int(n) for n in input("Enter the list A (column,row): ").split(',')]
b_col, b_row = [int(n) for n in input("Enter the list B (column,row): ").split(',')]
np.random.seed(1)
a = np.random.randn(a_col*a_row).reshape(a_col,a_row)
b = np.random.randn(b_col*b_row).reshape(b_col,b_row)

def matrix_multiplication (A, B):
    C = [[] for x in range(len(A))]
    if len(A[0]) != len(B):
        return (-1)
    else:
        for a in range(len(A)): # loops through number of rows
            for b in range(len(B[0])): # loops through number of elements
                TempSum = 0
                for c in range(len(B)): # caculates sum of (a,c) * (b,c) and addes the result to TempSum
                    TempSum += A[a][c] * B[c][b]
                C[a].append(TempSum) # appends TempSum to the correct spot
        return (C)

while True:
    print("\n")
    print("Loading... Please wait.")
    print ("\n")
    if matrix_multiplication(a,b) == -1:
        print ("ERROR")
        print ("\n")
        a_col, a_row = [int(n) for n in input("Enter the list A (column,row): ").split(',')]
        b_col, b_row = [int(n) for n in input("Enter the list B (column,row): ").split(',')]
        np.random.seed(1)
        a = np.random.randn(a_col*a_row).reshape(a_col,a_row)
        b = np.random.randn(b_col*b_row).reshape(b_col,b_row)
    else:
        C = matrix_multiplication(a,b)
        correct_C = a.dot(b)
        print ("Result: \n %s" % (C))
        print ("\n")
        print ("Result (column,row): %s, %s" % (len(C), len(C[0])))
        print ("\n")
        break

# checks if the two lists are the same
print ("Checking if the answer is correct:")
print(C[2][2])
print(correct_C[2][2])
print ("\n")
