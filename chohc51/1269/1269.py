from sys import *

n,m = map(int,stdin.readline().split())
n_set = set(map(int,stdin.readline().split()))
m_set = set(map(int,stdin.readline().split()))

x = n_set - m_set
y = m_set - n_set
result = x | y

print(len(result))