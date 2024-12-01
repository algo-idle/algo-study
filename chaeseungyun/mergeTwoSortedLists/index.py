# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        head = dummy
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
            else:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
        if list1 is None:
            dummy.next = list2
        if list2 is None:
            dummy.next = list1
        return head.next
