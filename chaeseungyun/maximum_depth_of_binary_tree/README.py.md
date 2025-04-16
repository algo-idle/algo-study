# Maximum Depth of Binary Tree

## 문제
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## 입력
```
root = [3,9,20,null,null,15,7]
```

## 출력
```
3
```
## 코드
```
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []

        head = root
        subHead = subroot

        stack.append(head)

        while stack:
            node = stack.pop()
```

## 채점 결과
![alt text](image.png)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)