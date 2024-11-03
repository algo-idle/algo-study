import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = [list(map(int, input().rstrip().split())) for _ in range(N)]

d = {}

for i in range(N):
    for j in range(N):
        buf = nums[i][0] + nums[j][1]
        if buf in d:
            d[buf] += 1
        else:
            d[buf] = 1

res = 0

for i in range(N):
    for j in range(N):
        buf = -1 * (nums[i][2] + nums[j][3])
        if buf in d:
            res += d[buf]

print(res)
