# 11779번: 최소비용 구하기 2 (골드 3)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  1초   | 256MB  |

## 문제
n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다.

## 문제 설명
```text
1. 그래프를 입력받는다.
2. 다익스트라를 수행한다. 이때 기존 다익스트라에서 경로를 추가로 기록하며 진행한다.
3. 다익스트라 결과를 출력한다.
```

## 입력
첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.

## 출력
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.

셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.


## 예제 입력 1 
```text
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
```

## 예제 출력 1 
```text
4
3
1 3 5
```


## 코드
```python
import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
graph = [[0 if i == j else 1e9 for j in range(N + 1)] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().strip().split())
    graph[a][b] = min(graph[a][b], c)

start, end = map(int, input().strip().split())

def dijkstra(start, end):
    distance = [[1e9, []] for _ in range(N + 1)]
    distance[start] = [0, [start]]
    heap = []
    heapq.heappush(heap, (0, start, [start]))
    while heap:
        dist, now, path = heapq.heappop(heap)
        if dist > distance[now][0]:
            continue
        for next in range(len(graph[now])):
            cost = dist + graph[now][next]
            if cost < distance[next][0]:
                distance[next] = [cost, path + [next]]
                heapq.heappush(heap, (cost, next, path + [next]))

    return distance[end]

cost, path = dijkstra(start, end)
print(cost, len(path), ' '.join(map(str, path)), sep='\n')

```

## 채점 결과
![img.png](img.png)

## 스트릭
![img_1.png](img_1.png)
