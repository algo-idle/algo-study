import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
res = abs(nums[0] + nums[-1])
pos = (nums[0], nums[-1])


front, rear = 0, N - 1
while front < rear:
    cur_sum = nums[front] + nums[rear]
    if abs(cur_sum) < res:
        res = abs(cur_sum)
        pos = (nums[front], nums[rear])

        if res == 0:
            break
    else:
        if cur_sum < 0:
            front += 1
        else:
            rear -= 1

print(*pos)