import sys
read = sys.stdin.readline

N, M = map(int, read().split())
nums = list(map(int, input().split()))
for i in range(1, N):
    nums[i] += nums[i-1]
nums.insert(0, 0)

for _ in range(M):
    start, end = map(int, read().split())
    print(nums[end] - nums[start - 1])