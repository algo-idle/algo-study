from collections import deque
def solution(maps):
    n = len(maps) #y축
    m = len(maps[0]) #x축
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    dx = [-1,1,0,0] #위,아래,왼쪽,오른쪽
    dy = [0,0,-1,1]
    visited[0][0] = True
    queue.append((0,0)) #(y,x축)
    
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n or maps[ny][nx] == 0:
                continue
            if not visited[ny][nx]:
                maps[ny][nx]= maps[y][x]+1
                visited[ny][nx] = 1
                queue.append((ny,nx))
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
                
