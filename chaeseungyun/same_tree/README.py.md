# same tree

## 문제
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
## 입력
```
p = [1,2,3], q = [1,2,3]
```
## 출력
```
true

```
## 코드
```
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
           # 두 노드가 모두 None이면 True
        if not p and not q:
            return True
        # 두 노드 중 하나만 None이면 False
        if not p or not q:
            return False
        # 현재 노드의 값이 다르면 False
        if p.val != q.val:
            return False
        # 좌측 및 우측 자식 노드를 재귀적으로 비교
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## 채점 결과
![alt text](image.png)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
leetcode 입니다