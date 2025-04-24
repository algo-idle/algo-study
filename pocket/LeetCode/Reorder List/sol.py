# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        start, end = head, head

        while end and end.next:
            start = start.next
            end = end.next.next

        prev, curr = None, start
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        start, end = head, prev
        while end.next:
            start.next, start = end, start.next
            end.next, end = start, end.next
