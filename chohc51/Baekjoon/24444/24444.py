from sys import *
from collections import deque
N,M,start = map(int,stdin.readline().split())
result = [0]*N
graph = [[] for _ in range(N)]
count = 1
q = deque([start-1])
for _ in range(M):
    a,b = map(int,stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
while q:
    point = q.popleft()

    if result[point] == 0:
        result[point] = count
        count+=1
    graph[point].sort()
    for x in graph[point][:]:
        graph[point].remove(x)
        graph[x].remove(point)
        q.append(x)
            
print(*result,sep='\n')
    
            
    