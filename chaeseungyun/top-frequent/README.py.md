#  Top K Frequent Elements

## 문제
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
## 입력
```
nums = [1,1,1,2,2,3], k = 2
```
## 출력
```
[1,2]
```
## 코드
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sortedList = sorted(freq, key=lambda num: freq[num])
        return sortedList[-k:]
```

## 채점 결과
![alt text](image.png)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
leetcode 입니다
