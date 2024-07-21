from sys import *
import math
start,end = map(int,stdin.readline().split())

for i in range(start,end+1):
    prime = True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            prime = False
            break
    if prime and i != 1:
        print(i)