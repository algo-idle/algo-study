import sys

read = sys.stdin.readline
N, M = map(int, read().split())
trees = list(map(int, read().split()))

start = 1
end = max(trees)
mid = 0

while True:
    mid = (start + end) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1
    if start <= end:
        continue
    break

print(end)