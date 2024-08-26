import math

num = int(input())

tmp = 1
result = 0
while tmp*tmp<=num:
    tmp+=1
    result+=1
print(result)