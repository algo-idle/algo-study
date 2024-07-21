from sys import *

n = int(stdin.readline())
register = set()
for _ in range(n):
    name,state= stdin.readline().split()
    if state == 'enter':
        register.add(name)
    elif state == 'leave':
        register.remove(name)
register = list(register)
register.sort(reverse=True)
for i in register:
    print(i)
