from sys import *

n,m = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

arr.sort(reverse=True)
print(arr[m-1])