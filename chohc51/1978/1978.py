from sys import *

num = int(stdin.readline())
arr= list(map(int,stdin.readline().split()))
count = 0
for i in arr:
    flag = False
    if i == 1:
        flag = True
    for x in range(2,i):
        if i % x == 0:
            flag = True
    if not flag:
        count+=1
print(count)
