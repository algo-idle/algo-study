# 104. Maximum Depth of Binary Tree

## 문제
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## 예제 입력 1
```text
root = [3,9,20,null,null,15,7]
```
## 예제 출력 1
```text
3
```
## 예제 입력 2
```text
root = [1,null,2]
```
## 예제 출력 2
```text
2
```

## 코드
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

```python
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height = 0
        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height += 1
        return height
```

## [채점 결과](https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1436376343)