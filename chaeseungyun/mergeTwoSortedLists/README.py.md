# Merge Two Sorted Lists

## 문제
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
## 입력
```
Input: list1 = [1,2,4], list2 = [1,3,4]
```
## 출력
```
Output: [1,1,2,3,4,4]
```
## 코드
```python
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
```

## 채점 결과
![alt text](image.png)
