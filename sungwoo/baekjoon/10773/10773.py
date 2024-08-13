import sys
read = sys.stdin.readline

K = int(read())
# l = [int(read()) for _ in range(K)]
stack = []
for _ in range(K):
    num = int(read())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))