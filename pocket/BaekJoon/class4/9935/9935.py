from collections import deque
import sys
input = sys.stdin.readline

S = deque(list(input().rstrip()))
boom = list(input().rstrip())
boom_length = len(boom)

stack = []

for s in S:
    stack.append(s)
    if stack[-boom_length:] == boom:
        for _ in range(boom_length):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')

