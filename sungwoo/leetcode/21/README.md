# 21. Merge Two Sorted Lists

## 문제
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## 예제 입력 1
```text
list1 = [1,2,4], list2 = [1,3,4]
```
## 예제 출력 1
```text
[1,1,2,3,4,4]
```
## 예제 입력 2
```text
list1 = [], list2 = []
```
## 예제 출력 2
```text
[]
```
## 예제 입력 3
```text
list1 = [], list2 = [0]
```
## 예제 출력 3
```text
[0]
```

## 코드
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return mergedList.next
```
### 코드 설명
- 병합된 정보를 저장할 새 연결 리스트를 생성한다.
 mergedList는 head의 정보를 유지하기 위함, tail은 노드를 계속 이어가기 위함.
- list1과 list2의 head 값이 존재할 때까지 두 값 중 작은 값을 tail의 next 값으로 지정하며 노드를 한칸씩 이동한다.
- 반복문이 종료되면 두 리스트 중 잔여 노드가 있는 리스트를 tail뒤에 잇는다.
- mergedList의 next값을 반환한다.(새로운 연결 리스트가 생성될 때 생성자로 인해 0 값을 갖는 노드가`head로 생성되었기 때문)
## [채점 결과](https://leetcode.com/problems/merge-two-sorted-lists/submissions/1433123197)