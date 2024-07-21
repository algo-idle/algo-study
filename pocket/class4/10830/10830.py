import sys
input = sys.stdin.readline


def matmul(A, B):

    res = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(A)):
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= 1000
    return res


N, B = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

def power(matrix, n):
    if n == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= 1000
        return matrix
    else:
        m = power(matrix, n // 2)
        if n % 2 == 0:
            return matmul(m, m)
        else:
            return matmul(matmul(m, m), matrix)


res = power(matrix, B)

for r in res:
    print(*r)
