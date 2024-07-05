from sys import *

num = int(stdin.readline().strip())
test = list(map(int,stdin.readline().split()))
stack = []

for i in range(1,num+1):
    if stack:
        if stack[-1] == i:
            del stack[-1]
            continue
    while test:
        if test[0] != i:
            stack.append(test[0])
            del test[0]
        else:
            del test[0]
            break

if not test and not stack:
    print("Nice")
else:
    print("Sad")
            
