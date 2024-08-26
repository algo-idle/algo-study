from sys import *

num = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))


print((sum(arr)*100)/(num*max(arr)))



