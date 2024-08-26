from sys import *

n,m = map(int,stdin.readline().split())
arr = [i+1 for i in range(n)]
for _ in range(m):
    a,b = map(int,stdin.readline().split())
    arr[b-1],arr[a-1] = arr[a-1],arr[b-1]
    
print(*arr)