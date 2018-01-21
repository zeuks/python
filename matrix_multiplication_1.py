A = [[3,4,5],
    [6,7,8],
    [9,10,11]]

B = [[2,4,8],
    [9,7,8],
    [6,5,10]]

def matrix_multiplication (A, B): # created function for easy caculation later on
    C = [[] for _ in range(len(A))] # creates the result list
    for a in range(len(A)): # loops through number of rows
        for b in range(len(B[0])): # loops through number of elements
            TempSum = 0
            for c in range(len(A[0])): # caculates sum of (a,c) * (b,c) and addes the result to TempSum
                TempSum += A[a][c] * B[c][b]
            C[a].append(TempSum)
    return (C)

print (matrix_multiplication(A, B))
