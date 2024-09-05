import sys
input = sys.stdin.readline

N = int(input().rstrip())
num_a = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
num_b = list(map(int, input().rstrip().split()))

res = []
while True:

    if not num_a or not num_b:
        break

    idx_a = num_a.index(max(num_a))
    idx_b = num_b.index(max(num_b))

    if num_a[idx_a] == num_b[idx_b]:
        res.append(num_a[idx_a])
        num_a = num_a[idx_a + 1:]
        num_b = num_b[idx_b + 1:]
    elif num_a[idx_a] > num_b[idx_b]:
        num_a.pop(idx_a)
    else:
        num_b.pop(idx_b)



print(len(res))
print(*res)