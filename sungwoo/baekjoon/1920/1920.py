import sys
read = sys.stdin.readline

N = int(read())
n_set = set(map(int, read().split()))
M = int(read())
m_list = list(map(int, read().split()))
for m in m_list:
    print(1 if m in n_set else 0)