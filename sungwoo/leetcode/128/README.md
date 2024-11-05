# 347. Top K Frequent Elements

## 문제
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


## 예제 입력 1
```text
nums = [100,4,200,1,3,2]
```
## 예제 출력 1
```text
4
```
## 예제 입력 2
```text
nums = [0,3,7,2,5,8,4,6,0,1]
```
## 예제 출력 2
```text
9
```

## 코드
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        result = [1]
        prev, cursor = nums[0], 0
        for num in nums:
            if num == prev:
                continue
            elif num == prev + 1:
                result[cursor] += 1
            else:
                cursor += 1
                result.append(1)
            prev = num
        return max(result)
```
### 코드 설명
- nums가 빈 리스트면 0을 반환한다.
- nums를 정렬한다.
- 정렬된 nums에서 연속된 숫자를 카운트 하며 값을 업데이트 한다.
- 연속된 숫자의 개수가 저장된 result에서 가장 큰 값을 반환한다.
## [채점 결과](https://leetcode.com/problems/longest-consecutive-sequence/submissions/1442558835)