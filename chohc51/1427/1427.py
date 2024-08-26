from sys import *

num = list((stdin.readline()))
num.sort(reverse=True)
print(*num,sep='')