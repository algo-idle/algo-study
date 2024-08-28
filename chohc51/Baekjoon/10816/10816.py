from sys import *

num = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
check = int(stdin.readline())
check_arr = list(map(int,stdin.readline().split()))
result = {}

for i in arr:
    if i in result:
        result[i] +=1
    else:
        result[i] = 1

for i in check_arr:
    if i in result:
        print(result[i],end=' ')
    else:
        print("0",end=' ')