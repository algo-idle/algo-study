import sys
read = sys.stdin.readline

while True:
    str = read().rstrip()
    if str == '.':
        break
    stack = []
    for x in str:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0 or stack[-1] != '(':
                stack.append(x)
                break
            else:
                stack.pop()
        elif x == ']':
            if len(stack) == 0 or stack[-1] != '[':
                stack.append(x)
                break
            else:
                stack.pop()
    print('yes' if len(stack) == 0 else 'no')