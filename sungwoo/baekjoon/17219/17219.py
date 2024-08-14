import sys
read = sys.stdin.readline

N, M = map(int, read().split())
notePad = dict()
for _ in range(N):
    url, pw = map(str, read().split())
    notePad[url] = pw

for _ in range(M):
    key = str(read().strip())
    print(notePad[key])