# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        now = head

        while list1 and list2:
            if list1.val < list2.val:
                now.next = list1
                list1 = list1.next
            else:
                now.next = list2
                list2 = list2.next
            now = now.next

        while list1:
            now.next = list1
            list1 = list1.next
            now = now.next

        while list2:
            now.next = list2
            list2 = list2.next
            now = now.next

        return head.next