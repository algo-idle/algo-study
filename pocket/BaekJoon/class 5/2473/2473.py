import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
nums.sort()

_sum = float('inf')
sel = None

for i in range(N - 2):
    front, rear = i + 1, N - 1
    while front < rear:
        s = nums[i] + nums[front] + nums[rear]
        if abs(s) < abs(_sum):
            _sum = s
            sel = (nums[i], nums[front], nums[rear])

        if s < 0:
            front += 1
        elif s > 0:
            rear -= 1
        else:
            break

print(*sel)
