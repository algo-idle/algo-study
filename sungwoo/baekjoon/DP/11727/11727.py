import sys
read = sys.stdin.readline

n = int(read())
memo = [1, 3]
for i in range(2, n):
    memo.append((2 * memo[i-2] + memo[i-1]) % 10007)
print(memo[n-1])