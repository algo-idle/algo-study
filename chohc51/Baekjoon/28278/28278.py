from sys import *

num = int(stdin.readline())
stack = []
for _ in range(num):
    tmp = list(map(int,stdin.readline().split()))
    command = tmp[0]
    if command == 1:
        stack.append(tmp[1])
    elif command== 2:
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif command== 3:
        print(len(stack))
    elif command== 4:
        if not stack:
            print("1")
        else:
            print("0")
    elif command== 5:
        if stack:
            print(stack[-1])
        else:
            print("-1")
    