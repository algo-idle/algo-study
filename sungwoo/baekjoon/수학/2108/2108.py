import sys
import math
from collections import Counter
read = sys.stdin.readline

N = int(read())
nums = [int(read()) for _ in range(N)]
result = [math.floor(sum(nums) / N + 0.5)]

nums.sort()
result.append(nums[math.floor(N/2)])

if len(nums) == 1:
    result.append(nums[0])
else:
    memo = Counter(nums).most_common(2)
    result.append(memo[1][0] if memo[0][1] == memo[1][1] else memo[0][0])

result.append(nums[-1] - nums[0])

print(*result, sep='\n')