import sys
read = sys.stdin.readline

N = int(read())
sang = list(map(int, read().split()))
M = int(read())
cards = list(map(int, read().split()))

sang_dic = {}
for i in sang:
    if i in sang_dic:
        sang_dic[i] += 1
    else:
        sang_dic[i] = 1
for i in cards:
    print(sang_dic[i], end=' ') if i in sang_dic else print(0, end=' ')