import sys
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
buf = list(map(int, input().rstrip().split()))
nums = [0 for _ in range(N + 1)]
nums[1] = buf[0]
for i in range(2, N + 1):
    nums[i] += nums[i - 1] + buf[i - 1]

front, rear = 0, 1
res = float('inf')

while True:
    s = nums[rear] - nums[front] if rear != front else nums[rear]
    if s < S:
        rear += 1
        if rear == N + 1:
            break
    else:
        res = min(res, rear - front if rear - front else 1)
        front += 1
        if rear < front:
            rear += 1
        if rear == N + 1:
            break

print(res if res != float('inf') else 0)
