# Product of Array Except Self

## 문제
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
## 입력
```
nums = [1,2,3,4]
```
## 출력
```
[24,12,8,6]
```
## 코드
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        up = [1] * len(nums)

        for i in range(len(nums) - 1):
            up[i + 1] = up[i] * nums[i]

        down = [1] * len(nums)

        for i in range(len(nums) - 1, 0, -1):
            down[i - 1] = down[i] * nums[i]

        result = []
        for x in zip(up, down):
            result.append(x[0] * x[1])
        
        return result

```

## 채점 결과
![alt text](image.png)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
leetcode 입니다