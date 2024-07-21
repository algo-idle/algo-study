# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        buf = {}
        while head is not None:
            try:
                return buf[(head.val, head.next)]
            except:
                pass
            buf[(head.val, head.next)] = True
            head = head.next

        return False