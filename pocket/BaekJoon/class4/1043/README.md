# 1043번: 거짓말(골드 4)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  2초   | 128MB  |

## 문제
지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다. 지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다. 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다. 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다. 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다. 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다. 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야 한다.

사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다. 지민이는 모든 파티에 참가해야 한다. 이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

## 문제 설명
```text
1. 파티에 가는 친구의 아이디를 저장한다.
2. 친구(u)가 가는 파티를 {u: list()} 형태로 저장한다.
3. 파티(p)에 오는 친구를 {p: list()} 형태로 저장한다.
4. bfs를 통해 친구(u)가 간 파티를 순회하며 visit = True로 하고, 동시에 파티(p)에 간 친구들을 deque에 append한다.
5. bfs가 끝나면 visit하지 않은 파티의 수를 출력한다.
```

## 입력
첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.

둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.

셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

## 출력
첫째 줄에 문제의 정답을 출력한다.


## 예제 입력 1 
```text
4 3
0
2 1 2
1 3
3 2 3 4
```
## 예제 출력 1 
```text
3
```
## 예제 입력 2 
```text
4 1
1 1
4 1 2 3 4
```
## 예제 출력 2
```text
0
```
## 예제 입력 3
```text
4 1
0
4 1 2 3 4
```
## 예제 출력 3
```text
1
```
## 예제 입력 4
```text
4 5
1 1
1 1
1 2
1 3
1 4
2 4 1
```
## 예제 출력 4
```text
2
```
## 예제 입력 5
```text
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4
```
## 예제 출력 5
```text
4
```
## 예제 입력 6
```text
8 5
3 1 2 7
2 3 4
1 5
2 5 6
2 6 8
1 8
```
## 예제 출력 6
```text
5
```
## 예제 입력 7
```text
3 4
1 3
1 1
1 2
2 1 2
3 1 2 3
```
## 예제 출력 7
```text
0
```

## 코드
```python
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
know = list(map(int, input().rstrip().split()))

if know == [0]:
    print(M)
    exit(0)

know.pop(0)
user_visit = [False for _ in range(N + 1)]
party_visit = [False for _ in range(M)]

for k in know:
    user_visit[k] = True

user_party = {u: [] for u in range(1, N + 1)}
party_user = {p: [] for p in range(M)}

for i in range(M):
    user_ids = list(map(int, input().rstrip().split()))[1:]
    party_user[i] = user_ids
    for user_id in user_ids:
        user_party[user_id].append(i)

q = deque([k for k in know])
while q:
    u = q.popleft()

    for party in user_party[u]:
        if not party_visit[party]:
            party_visit[party] = True
            for user in party_user[party]:
                if not user_visit[user]:
                    user_visit[user] = True
                    q.append(user)

print(party_visit.count(False))
```

## 채점 결과
![img.png](img.png)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/82014995/5a014e9d-1092-4c9f-a538-754382558d72)
