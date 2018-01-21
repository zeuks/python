A = [[3,4,5],
    [6,7,8],
    [9,10,11]]

B = [[2,4,8],
    [9,7,8],
    [6,5,10]]

def matrix_multiplication (A, B):
    C = [[] for _ in range(len(A))]
    for a in range(len(A)):
        for b in range(len(B[0])):
            TempSum = 0
            for c in range(len(B[0])):
                TempSum += A[a][c] * B[c][b]
            C[a].append(TempSum)
    return (C)

print (matrix_multiplication(A, B))
