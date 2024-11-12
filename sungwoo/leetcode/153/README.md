# 153. Find Minimum in Rotated Sorted Array

## 문제
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


## 예제 입력 1
```text
nums = [3,4,5,1,2]
```
## 예제 출력 1
```text
1
```
## 예제 입력 2
```text
nums = [4,5,6,7,0,1,2]
```
## 예제 출력 2
```text
0
```
## 예제 입력 3
```text
nums = [11,13,15,17]
```
## 예제 출력 3
```text
11
```

## 코드
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
```
### 코드 설명
- 리스트의 첫번째 숫자가 마지막 숫자보다 작은 경우 회전이 되지 않았다는 것이므로 가장 첫번째 요소를 반환한다.
- left, right를 설정하고 두 값의 중간인 mid를 계산한다.

- 두가지 경우가 있다.
   - mid값보다 right값이 큰 경우: mid ~ right는 정렬되어 있음 = 최솟값이 mid+1과 right사이에 존재하지 않음.
   - mid값이 right값보다 큰 경우: mid ~ right는 정렬되어 있지 않음 = 최솟값이 mid와 right사이에 존재함.
- left와 right가 같아질 때 까지 반복한다.
## [채점 결과](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1448463930)