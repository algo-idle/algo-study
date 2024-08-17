min_num = int(input())
max_num = int(input())
target = -1
count = 0

for i in range(max_num,min_num-1,-1):
    if i == 1:
        continue
    if i == 2:
        target = i
        count += i
    for x in range(2,i):
        if i%x == 0:
            break
        if x == i-1:
            target = i
            count += i

if target == -1:
    print(target)
else:
    print(count)
    print(target)
    