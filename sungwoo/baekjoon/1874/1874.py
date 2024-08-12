import sys
read = sys.stdin.readline

n = int(read())
t = [int(read()) for _ in range(n)]
stack = [1]
result = ['+']
cursor = 0
curr = 2

while cursor < n:
    if stack:
        if t[cursor] == stack[-1]:
            stack.pop()
            result.append('-')
            cursor += 1
        elif t[cursor] > stack[-1]:
            stack.append(curr)
            curr += 1
            result.append('+')
        else:
            result.clear()
            break
    else:
        if t[cursor] >= curr:
            stack.append(curr)
            curr += 1
            result.append('+')
        else:
            result.clear()
            break

if result:
    for i in result:
        print(i)
else:
    print('NO')