import sys
input = sys.stdin.readline


def matmul(A, B):

    res = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B[0])):
            for j in range(len(A)):
                res[i][k] += A[i][j] * B[j][k]
            res[i][k] %= 1000000007
    return res

def power(matrix, n):
    if n == 1:
        for i in range(2):
            for j in range(2):
                matrix[i][j] %= 1000
        return matrix
    else:
        m = power(matrix, n // 2)
        if n % 2 == 0:
            return matmul(m, m)
        else:
            return matmul(matmul(m, m), matrix)

N = int(input())
matrix = [[1, 1], [1, 0]]
start = [[1], [1]]
if N < 3:
    print(1)
else:
    print(matmul(power(matrix, N - 2), start)[0][0])
