import sys
read = sys.stdin.readline

N = int(read())
S = 0
for _ in range(N):
    line = str(read())
    op = line.split()
    if op[0] == "add":
        S |= (1 << int(op[1]))
    elif op[0] == "remove":
        S &= ~(1 << int(op[1]))
    elif op[0] == "check":
        print(1 if S & (1 << int(op[1])) else 0)
    elif op[0] == "toggle":
        S ^= (1 << int(op[1]))
    elif op[0] == "all":
        S = 2097151
    elif op[0] == "empty":
        S = 0