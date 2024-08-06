# 1697번: 숨바꼭질(실버 1)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  1초   | 256MB  |

## 문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

## 입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

## 출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

## 예제 입력 1
```text
5 17
```
## 예제 출력 1
```text
4
```

## 코드
```python
import sys
from collections import deque

read = sys.stdin.readline
N, K = map(int, read().split())
visited_time = [0] * 100001

que = deque()
que.append(N)
while que:
    n = que.popleft()
    if n == K:
        print(visited_time[n])
        break
    for i in (n-1, n+1, n*2):
        if 0 <= i <= 100000 and not visited_time[i]:
            visited_time[i] = visited_time[n] + 1
            que.append(i)
```

## 채점 결과
![image](result_img.png)

## 스트릭
![image](streak_img.png)