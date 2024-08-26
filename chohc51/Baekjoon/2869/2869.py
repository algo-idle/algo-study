
from sys import *
import math
climb,slip,end = map(int,stdin.readline().split())
count = 1
if climb>=end:
    print(count)
else: #climb +(climb-slip)*n >= end에서 n이 일수(첫 climb는 1로 카운트)
    n = math.ceil((end-climb)/(climb-slip))
    count+= n
    print(count)

    

