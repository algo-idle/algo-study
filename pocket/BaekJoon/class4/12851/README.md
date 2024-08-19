# 12851번: 숨바꼭질 2 (골드 4)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  2초   | 512MB  |

## 문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

## 문제 설명
```text
1. 방문배열을 True/False의 boolean값이 아닌 최단거리 값인 int값으로 하여 사용한다.
2. 방문한 적 없다면, 현재 거리 + 1의 값을 저장하고, 방문한 적이 있으며 현재 거리 + 1과 값이 같다면 (최단거리라면) 해당 노드를 방문한다.
3. 현재 노드가 K(동생의 위치)라면 cnt를 1 증가한다.
```

## 입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.


## 출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.


## 예제 입력 1 
```text
5 17
```

## 예제 출력 1 
```text
4
2
```


## 코드
```python
from collections import deque

N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
q = deque([N])
visited[N] = 1
cnt = 0

while q:
    pos = q.popleft()
    if pos == K:
        cnt += 1
    else:
        for new_pos in [pos + 1, pos - 1, pos * 2]:
            if 0 <= new_pos <= 100000:
                if visited[new_pos] == 0:
                    visited[new_pos] = visited[pos] + 1
                    q.append(new_pos)
                elif visited[new_pos] == visited[pos] + 1:
                    q.append(new_pos)

print(visited[K] - 1)
print(cnt)
```

## 채점 결과
![img.png](img.png)

## 스트릭
![img_1.png](img_1.png)
