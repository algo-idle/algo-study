import sys
read = sys.stdin.readline

N = int(read())
words = list(set(list(read().rstrip() for _ in range(N))))
for word in sorted(sorted(words), key=len):
    print(word)