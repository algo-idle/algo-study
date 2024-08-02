from sys import *
num = int(stdin.readline())
arr = set()
for _ in range(num):
    arr.add(stdin.readline().rstrip())

arr = list(arr)
arr.sort()
arr.sort(key = lambda x: (len(x),x[0]))

for i in arr:
    print(i)