import sys
read = sys.stdin.readline

N, K = map(int, read().split())
coins = [int(read()) for _ in range(N)]
count = 0
for coin in reversed(coins):
    x = K // coin
    if x > 0:
        K -= x * coin
        count += x
print(count)