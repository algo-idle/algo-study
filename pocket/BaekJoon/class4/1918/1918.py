S = input()

stack = []
res = ''

for s in S:
    if s == '(':
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()
    elif s in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            res += stack.pop()
        stack.append(s)
    elif s in ['+', '-']:
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(s)
    else:
        res += s

while stack:
    res += stack.pop()

print(res)
