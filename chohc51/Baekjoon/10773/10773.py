num = int(input())
count = 0
stack = []
for _ in range(num):
    value = int(input())
    if value == 0:
        stack.pop()
    else:
        stack.append(value)
        
print(sum(stack))
    