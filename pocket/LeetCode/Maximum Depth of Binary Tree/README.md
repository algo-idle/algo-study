# Maximum Depth of Binary Tree

## 문제
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## 문제 설명
```text
1. 노드를 순회하면서 가장 깊은 곳의 깊이를 반환한다.
```

## Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

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
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

## 채점 결과
![img.png](img.png)

## 스트릭
![img_1.png](img_1.png)g
