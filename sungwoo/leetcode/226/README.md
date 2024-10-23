# 226. Invert Binary Tree

## 문제
Given the root of a binary tree, invert the tree, and return its root.


## 예제 입력 1
```text
root = [4,2,7,1,3,6,9]
```
## 예제 출력 1
```text
[4,7,2,9,6,3,1]
```
## 예제 입력 2
```text
root = [2,1,3]
```
## 예제 출력 2
```text
[2,3,1]
```
## 예제 입력 3
```text
root = []
```
## 예제 출력 3
```text
[]
```

## 코드
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```
### 코드 설명
- 해당 노드가 자식을 가지지 않을 때까지 재귀적으로 left값, right값을 바꾼다.
## [채점 결과](https://leetcode.com/problems/invert-binary-tree/submissions/1431242823)