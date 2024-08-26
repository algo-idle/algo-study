from sys import *

n,m = map(int,stdin.readline().split())
hear_name_list = set()
see_name_list = set()

for _ in range(n):
    name = stdin.readline().rstrip()
    hear_name_list.add(name)
for _ in range(m):
    name = stdin.readline().rstrip()
    see_name_list.add(name)
    
result = hear_name_list & see_name_list
result = list(result)
result.sort()

print(len(result))
for i in result:
    print(i)