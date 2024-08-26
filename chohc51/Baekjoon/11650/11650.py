from sys import *
num = int(stdin.readline())
arr = []
for _ in range(num):
    tmp = list(map(int,stdin.readline().split()))
    arr.append(tmp)
arr.sort(key=lambda x:(x[0],x[1]))
for i in arr:
    print(*i)