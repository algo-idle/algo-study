import sys
import math
read = sys.stdin.readline

n = int(read())
m = list(map(int, str(math.factorial(n))))
result = 0
for i in reversed(m):
    if i == 0:
        result += 1
    else:
        break
print(result)