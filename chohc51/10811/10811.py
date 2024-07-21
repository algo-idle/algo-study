from sys import *

n,m = map(int,stdin.readline().split())
arr = [i for i in range(n+1)]

for _ in range(m):
    start,end = map(int,stdin.readline().split())
    tmp = arr[start:end+1]
    tmp.reverse()
    arr[start:end+1] = tmp
        
        
        
print(*arr[1:])