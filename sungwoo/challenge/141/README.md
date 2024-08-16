# 141. Linked List Cycle

## 문제
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## 예제 입력 1
```text
head = [3,2,0,-4], pos = 1
```
## 예제 출력 1
```text
true
```
## 예제 입력 2
```text
head = [1,2], pos = 0
```
## 예제 출력 2
```text
true
```
## 예제 입력 3
```text
head = [1], pos = -1
```
## 예제 출력 3
```text
false
```

## 코드
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```
### 코드 설명

- 연결 리스트가 존재하지 않거나 하나만 존재하는 경우 예외처리
- fast는 반복문이 한번 돌아갈 동안 두칸, slow는 한칸 이동시킨다. fast와 slow가 같으면 순환이 존재하므로 True 반환.
- 존재하지 않으면 반복문을 탈출해 False 반환


## 채점 결과
![image](result_img.png)
