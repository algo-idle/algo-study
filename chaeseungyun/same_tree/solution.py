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