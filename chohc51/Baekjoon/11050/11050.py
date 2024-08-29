from sys import *

a,b = map(int,stdin.readline().split())
up = 1
down = 1
if (a//2)<b:
    b = a-b
for _ in range(b):
    up = up*a
    a -=1
for _ in range(b):
    down = down*b
    b-=1

print(up//down)

