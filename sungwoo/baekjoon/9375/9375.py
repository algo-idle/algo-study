import sys
read = sys.stdin.readline

t = int(read())

for _ in range(t):
    n = int(read())
    closet = dict()
    for _ in range(n):
        name, type = map(str, read().split())
        if type in closet:
            closet[type].append(name)
        else:
            closet[type] = [name]
    count = 1
    for type in closet:
        count *= (len(closet[type]) + 1)
    print(count-1)