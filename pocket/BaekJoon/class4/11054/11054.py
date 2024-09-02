import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
B = list(reversed(A))
dp_A = [1 for _ in range(N)]
dp_B = [1 for _ in range(N)]


for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_A[i] = max(dp_A[i], dp_A[j] + 1)
        if B[i] > B[j]:
            dp_B[i] = max(dp_B[i], dp_B[j] + 1)

res = 0
for i in range(N):
    res = max(res, dp_A[i] + dp_B[N - 1 - i] - 1)

print(res)