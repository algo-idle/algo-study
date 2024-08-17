import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
value = [int(input().rstrip()) for _ in range(n)]
table = [0 for _ in range(k + 1)]
table[0] = 1

for i in range(n):
    for j in range(value[i], k + 1):
        table[j] += table[j - value[i]]

print(table[-1])
