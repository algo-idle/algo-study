import sys
import math
read = sys.stdin.readline

n = int(read())
table = [int(read()) for _ in range(n)]

table.sort()
x = math.floor(n * 0.15 + 0.5)
print(math.floor(sum(table[x:n-x]) / (n - 2 * x) + 0.5) if n != 0 else 0)