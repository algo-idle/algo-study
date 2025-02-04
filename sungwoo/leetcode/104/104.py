# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     height = 0
    #     queue = deque()
    #     queue.append(root)
    #     while queue:
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         height += 1
    #     return height