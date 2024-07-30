class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []

        head = root
        subHead = subroot

        stack.append(head)

        while stack:
            node = stack.pop()