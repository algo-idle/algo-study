from sys import *
from collections import deque

num = int(stdin.readline())
q = deque()

for _ in range(num):
    arr = list(stdin.readline().rstrip().split())
    if arr[0] == 'push':
        q.append(int(arr[1]))
    elif arr[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print("-1")
        
    elif arr[0] == 'size':
        print(len(q))
        
    elif arr[0] == 'empty':
        if q:
            print("0")
        else:
            print("1")
    elif arr[0] == 'front':
        if q:
            print(q[0])
        else:
            print("-1") 
    elif arr[0] == 'back':
        if q:
            print(q[-1])
        else:
            print("-1")
    