16724번: 피리 부는 사나이 (골드 3)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  1초   | 256MB  |

## 문제
피리 부는 사나이 성우는 오늘도 피리를 분다.

성우가 피리를 불 때면 영과일 회원들은 자기도 모르게 성우가 정해놓은 방향대로 움직이기 시작한다. 성우가 정해놓은 방향은 총 4가지로 U, D, L, R이고 각각 위, 아래, 왼쪽, 오른쪽으로 이동하게 한다.

이를 지켜보던 재훈이는 더 이상 움직이기 힘들어하는 영과일 회원들을 지키기 위해 특정 지점에 ‘SAFE ZONE’ 이라는 최첨단 방음 시설을 만들어 회원들이 성우의 피리 소리를 듣지 못하게 하려고 한다. 하지만 예산이 넉넉하지 않은 재훈이는 성우가 설정해 놓은 방향을 분석해서 최소 개수의 ‘SAFE ZONE’을 만들려 한다. 

성우가 설정한 방향 지도가 주어졌을 때 재훈이를 도와서 영과일 회원들이 지도 어느 구역에 있더라도 성우가 피리를 불 때 ‘SAFE ZONE’에 들어갈 수 있게 하는 ‘SAFE ZONE’의 최소 개수를 출력하는 프로그램을 작성하시오.

## 문제 설명
```text
1. dfs로 순환구조의 수를 찾으면 된다.
2. 이때 순환 구조가 아니라도, 순환구조로부터 뻗어나온 가지 또한 같은 순환 구조로 판단하고 처리한다.
```

## 입력
첫 번째 줄에 지도의 행의 수를 나타내는 N(1 ≤ N ≤ 1,000)과 지도의 열의 수를 나타내는 M(1 ≤ M ≤ 1,000)이 주어진다.

두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열이 주어진다.

지도 밖으로 나가는 방향의 입력은 주어지지 않는다.


## 출력
첫 번째 줄에 ‘SAFE ZONE’의 최소 개수를 출력한다.






## 예제 입력 1 
```text
3 4
DLLL
DRLU
RRRU
```
## 예제 출력 1 
```text
2
```

## 코드
```python
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
grid = [list(input().rstrip()) for _ in range(N)]
visit = [[-1 for _ in range(M)] for _ in range(N)]

direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def sol(x, y, idx):
    global answer
    if visit[x][y] != -1:   # 방문함
        if visit[x][y] == idx:
            answer += 1
        return

    visit[x][y] = idx
    i = direction.index(grid[x][y])
    sol(x + dx[i], y + dy[i], idx)

idx = 0
answer = 0
for n in range(N):
    for m in range(M):
        sol(n, m, idx)
        idx += 1

print(answer)

```

## 채점 결과
![img.png](img.png)

## 스트릭
![img_1.png](img_1.png)