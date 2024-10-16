import sys
read = sys.stdin.readline

N = int(read())
peoples = []
for _ in range(N):
    weight, height = map(int, read().split())
    peoples.append([weight, height])

for i in range(N):
    count = 1
    for j in range(N):
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            count += 1
    print(count, end=' ')