# 100. Same Tree

## 문제
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## 예제 입력 1
```text
p = [1,2,3], q = [1,2,3]
```
## 예제 출력 1
```text
true
```
## 예제 입력 2
```text
p = [1,2], q = [1,null,2]
```
## 예제 출력 2
```text
false
```
## 예제 입력 3
```text
p = [1,2,1], q = [1,1,2]
```
## 예제 출력 3
```text
false
```

## 코드
```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### 코드 설명
- p와 q가 모두 None인 경우 두 트리 모두 해당 위치에 노드가 존재하지 않는다는 뜻이므로 True를 반환한다.
- 둘 중 하나라도 None인 경우 두 트리 중 하나만 해당 위치에 노드가 존재한다는 뜻이므로 False를 반환한다.
- 두 노드가 같은 값을 가지지 않는 경우 False를 반환한다.
- 위 조건이 아니라면 함수를 재귀 호출한다.



```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueP, queueQ = deque(), deque()
        queueP.append(p), queueQ.append(q)
        while queueP and queueQ:
            p_down, q_down = queueP.popleft(), queueQ.popleft()
            if not p_down and not q_down:
                continue
            if not p_down or not q_down or p_down.val != q_down.val:
                return False
            queueP.append(p_down.left), queueP.append(p_down.right)
            queueQ.append(q_down.left), queueQ.append(q_down.right)
        return not queueP and not queueQ
```
### 코드 설명
- 트리 p에대한 큐와 q에 대한 큐를 각각 만들어 각 트리의 head를 큐에 삽입 후 BFS를 시작한다.
- 각 큐에서 꺼낸 노드 값이 모두 None인 경우 스킵한다.(해당 노드가 존재하지 않으므로 비교할 필요 X)
- 꺼낸 두 노드중 하나라도 None인 경우(1)와 두 노드의 값이 같지 않은 경우(2) False를 반환한다.
 
(1) 어떤 트리에는 노드가 존재하지만 다른 트리에는 노드가 존재하지 않음.

(2) 두 트리 모두 같은 위치에 노드가 존재하지만 값이 다름.
- 탐색이 끝난 후 두 큐가 모두 비어있다면 True를 반환한다.
## [채점 결과](https://leetcode.com/problems/same-tree/submissions/1435993520)