import sys
read = sys.stdin.readline

s = list(str(read().rstrip()))
memo = [-1 for _ in range(26)]
for i in reversed(range(len(s))):
  memo[ord(s[i]) - 97] = i

for i in range(26):
    print(memo[i], end=' ')