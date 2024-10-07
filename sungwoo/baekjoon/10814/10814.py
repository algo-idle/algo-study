import sys
read = sys.stdin.readline

N = int(read())
member_list = {}
for _ in range(N):
    age, name = map(str, read().split())
    age = int(age)
    if age not in member_list:
        member_list[age] = [name]
    else:
        member_list[age].append(name)

for (age, members) in sorted(member_list.items(), key=lambda x: x[0]):
    for member in members:
        print(age, member)
