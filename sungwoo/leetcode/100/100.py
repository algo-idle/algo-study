#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
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

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     queueP, queueQ = deque(), deque()
    #     queueP.append(p), queueQ.append(q)
    #     while queueP and queueQ:
    #         p_down, q_down = queueP.popleft(), queueQ.popleft()
    #         if not p_down and not q_down:
    #             continue
    #         if not p_down or not q_down or p_down.val != q_down.val:
    #             return False
    #         queueP.append(p_down.left), queueP.append(p_down.right)
    #         queueQ.append(q_down.left), queueQ.append(q_down.right)
    #     return not queueP and not queueQ