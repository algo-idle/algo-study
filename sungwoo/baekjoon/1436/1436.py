import sys
read = sys.stdin.readline

N = int(read())
title = 666
series = 0

while series < N:
    if '666' in str(title):
        series += 1
    title += 1
print(title-1)