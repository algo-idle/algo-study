import sys
read = sys.stdin.readline

N = int(read())
stack = []
for _ in range(N):
    command = read().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0) if stack else print(1)
    elif command[0] == 'top':
        print(stack[-1]) if stack else print(-1)