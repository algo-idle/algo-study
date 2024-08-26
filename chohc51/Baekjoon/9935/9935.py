from sys import *

test = list(stdin.readline().rstrip())
remove_word = list(stdin.readline().rstrip())
stack = []

for i in test:
    stack.append(i)
    if stack[len(stack)-len(remove_word):len(stack)] == remove_word:
        for _ in range(len(remove_word)):
            stack.pop()
if stack:
    print(*stack,sep='')
else:
    print("FRULA")
