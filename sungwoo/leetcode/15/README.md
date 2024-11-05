# 15. 3Sum

## 문제
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


## 예제 입력 1
```text
nums = [-1,0,1,2,-1,-4]
```
## 예제 출력 1
```text
[[-1,-1,2],[-1,0,1]]
```
## 예제 입력 2
```text
nums = [0,1,1]
```
## 예제 출력 2
```text
[]
```
## 예제 입력 3
```text
nums = [0,0,0]
```
## 예제 출력 3
```text
[[0,0,0]]
```

## 코드
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        if nums[0] > 0 or nums[-1] < 0:
            return result
        for start in range(len(nums) - 2):
            if nums[start] > 0:
                break
            if start > 0 and nums[start - 1] == nums[start]:
                continue
            left, right = start + 1, len(nums) - 1
            while left < right:
                total = nums[start] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[start], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

```
### 코드 설명
- 리스트에서 가장 작은 수가 양수거나 가장 큰 수가 음수면 합이 0이 될 수가 없으므로 빈 리스트를 반환한다.
- nums[start]가 양수면 탐색 중단.(위와 같은 이유)
- start, left, right에 대해 중복을 스킵한다.
- 반복문 순서 변경. 테스트케이스별로 다른 결과를 가지지만 대부분의 경우 합이 0임을 찾은 경우보다 포인터를 이동하며 탐색하는 경우가 많다고 생각해 순서를 변경해보았다.(실제로 실행시간이 줄었다!)
## [채점 결과](https://leetcode.com/problems/3sum/submissions/1443668495)