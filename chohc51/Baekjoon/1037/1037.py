from sys import *

num = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))

max_num,min_num = max(arr),min(arr)
print(max_num*min_num)
