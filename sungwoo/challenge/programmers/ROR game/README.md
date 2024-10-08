# 게임 맵 최단거리

## 문제
ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다. 다음은 5 x 5 크기의 맵에, 당신의 캐릭터가 (행: 1, 열: 1) 위치에 있고, 상대 팀 진영은 (행: 5, 열: 5) 위치에 있는 경우의 예시입니다.

![img.png](img.png)

위 그림에서 검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 흰색 부분은 갈 수 있는 길입니다. 캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없습니다.
아래 예시는 캐릭터가 상대 팀 진영으로 가는 두 가지 방법을 나타내고 있습니다.

- 첫 번째 방법은 11개의 칸을 지나서 상대 팀 진영에 도착했습니다.

![img_1.png](img_1.png)

- 두 번째 방법은 15개의 칸을 지나서 상대팀 진영에 도착했습니다.

![img_2.png](img_2.png)

위 예시에서는 첫 번째 방법보다 더 빠르게 상대팀 진영에 도착하는 방법은 없으므로, 이 방법이 상대 팀 진영으로 가는 가장 빠른 방법입니다.

만약, 상대 팀이 자신의 팀 진영 주위에 벽을 세워두었다면 상대 팀 진영에 도착하지 못할 수도 있습니다. 예를 들어, 다음과 같은 경우에 당신의 캐릭터는 상대 팀 진영에 도착할 수 없습니다.

![img_3.png](img_3.png)

게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

## 제한사항
maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.


## 예제 입력 1
```text
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
```
## 예제 출력 1
```text
11
```
## 예제 입력 2
```text
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
```
## 예제 출력 2
```text
-1
```

## 코드
```python
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(maps):
    height = len(maps)
    width = len(maps[0])
    memo = [[999 for _ in range(width)] for _ in range(height)]
    memo[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        val = memo[y][x]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < width and 0 <= ny < height:
                if maps[ny][nx] == 1 and val + 1 < memo[ny][nx]:
                    memo[ny][nx] = val + 1
                    queue.append((nx, ny))
    answer = memo[height - 1][width - 1] if memo[height - 1][width - 1] != 999 else -1
    return answer
```
### 코드 설명

- maps 의 크기와 동일한 테이블 생성. 이 테이블에는 해당 칸에 가기위한 최단 거리가 저장됨.
- 시작 위치(0, 0)을 큐에 삽입 후 bfs 시작. 인접한 칸이 뚫려있고(=1), 자신을 통한 경로가 더 짧은 경우 값 업데이트, 큐에 삽입.
- 탐색이 끝난 후 도착 위치(height-1, width-1)에 해당하는 값 반환. 값이 999면 도착하지 못했다는 것이므로 -1 반환.


## 채점 결과
![image](result_img.png)
