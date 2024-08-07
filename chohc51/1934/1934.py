from sys import *
import math
num = int(stdin.readline())
for _ in range(num):
    a,b = map(int,stdin.readline().split())
    tmp = math.gcd(a,b)
    if tmp == min(a,b):
        print(max(a,b))
    elif tmp == min(a,b):
        print(a*b)
    else:
        print(a*b//tmp)
    