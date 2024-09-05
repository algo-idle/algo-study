from collections import deque # 덱을 큐로 사용

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)] # 방문한 기록을 담는 2차원 배열
    
    queue = deque()
    queue.append((0,0,1)) # x, y, 길이
    visited[0][0] = True
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        x, y, cnt = queue.popleft()
        if x == n - 1 and y == m - 1:
            return cnt # 최종 거리 출력
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]: # 중복되지 않은 이동할 수 있는 값을 큐에 추가
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
        
    return -1 # 못찾으면 -1 반환