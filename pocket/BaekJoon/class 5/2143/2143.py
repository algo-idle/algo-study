import bisect
import sys
input = sys.stdin.readline

T = int(input().rstrip())
N = int(input().rstrip())
a_nums = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
b_nums = list(map(int, input().rstrip().split()))
ans = 0

a_prefix_sum = []
for l in range(1, N + 1):
    for i in range(N - l + 1):
        a_prefix_sum.append(sum(a_nums[i:i + l]))

a_prefix_sum.sort()

b_prefix_sum = []
for l in range(1, M + 1):
    for i in range(M - l + 1):
        b_prefix_sum.append(sum(b_nums[i:i + l]))

b_prefix_sum.sort()

for an in a_prefix_sum:
    left = bisect.bisect_left(b_prefix_sum, T - an)
    right = bisect.bisect_right(b_prefix_sum, T - an)
    ans += right - left

print(ans)
