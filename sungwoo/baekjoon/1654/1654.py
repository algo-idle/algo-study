import sys
read = sys.stdin.readline

K, N = map(int, read().split())
cables = [int(read()) for _ in range(K)]
front = 1
back = max(cables)
while True:
    count = 0
    mid = (front + back) // 2
    for cable in cables:
        count += cable // mid
    if front > back:
        break
    elif count >= N:
        front = mid + 1
    elif count < N:
        back = mid - 1
print(mid)