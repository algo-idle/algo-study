from sys import *
num = int(stdin.readline())
arr = []
for _ in range(num):
    age,name = list(stdin.readline().split())
    age = int(age)
    arr.append((age,name))
arr.sort(key=lambda x:x[0])
for i in arr:
    print(*i)
    
    
    