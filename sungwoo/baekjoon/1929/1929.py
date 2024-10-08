import sys
input = sys.stdin.readline

M, N = map(int, input().split())

nums = [True] * (N + 1)
nums[0] = nums[1] = False

for i in range(2, int(N**0.5) + 1):
    if nums[i]:
        for j in range(i * i, N + 1, i):
            nums[j] = False

for i in range(M, N + 1):
    if nums[i]:
        print(i)