import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
res = {n: 0 for n in nums}
MAX_NUM = max(nums)
nums.sort()

for num in nums:
    for j in range(num * 2, MAX_NUM + 1, num):
        if j in res:
            res[num] += 1
            res[j] -= 1

for v in res.values():
    print(v, end=' ')
