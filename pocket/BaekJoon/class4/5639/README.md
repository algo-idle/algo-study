# 5639번: 이진 검색 트리(골드 4)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  1초   | 256MB  |

## 문제
이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.

노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.


전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고, 왼쪽 서브트리, 오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다. 후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다. 예를 들어, 위의 이진 검색 트리의 전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고, 후위 순회 결과는 5 28 24 45 30 60 52 98 50 이다.

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

## 문제 설명
```text

```

## 입력
트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

## 출력
입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.


## 예제 입력 1 
```text
50
30
24
5
28
45
98
52
60
```
## 예제 출력 1 
```text
5
28
24
45
30
60
52
98
50
```


## 코드
```python
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**4)

tree = {}


def find(node, target):
    if 'val' in node.keys():
        if target < node['val']:
            if 'left' in node.keys():
                find(node['left'], target)
            else:
                node['left'] = {'val': target}
        else:
            if 'right' in node.keys():
                find(node['right'], target)
            else:
                node['right'] = {'val': target}
    else:
        node['val'] = target


def dfs(node):
    if 'left' in node.keys():
        dfs(node['left'])
        print(node['left']['val'])
    if 'right' in node.keys():
        dfs(node['right'])
        print(node['right']['val'])


while True:
    try:
        num = int(input().rstrip())
        find(tree, num)
    except:
        break

dfs(tree)
print(tree['val'])

```

## 채점 결과
![img.png](img.png)

## 스트릭
![img_1.png](img_1.png)