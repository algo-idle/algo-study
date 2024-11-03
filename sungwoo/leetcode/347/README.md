# 347. Top K Frequent Elements

## 문제
GGiven an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


## 예제 입력 1
```text
nums = [1,1,1,2,2,3], k = 2
```
## 예제 출력 1
```text
[1, 2]
```
## 예제 입력 2
```text
nums = [1], k = 1
```
## 예제 출력 2
```text
[1]
```

## 코드
```python
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
        sorted_list = sorted(dict.items(), key=lambda x:x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_list[i][0])
        return result
```
### 코드 설명
- 리스트를 순회하며 해당 숫자가 딕셔너리에 key로 존재하면 해당 값에 1을 더한다.
 존재하지 않는다면 딕셔너리에 해당 숫자를 key로 추가한 후에 value를 1로 설정한다.
- 딕셔너리를 해당 숫자 출현 횟수를 기준으로 내림차순 정렬 후 k만큼 추출해 result배열에 추가한다.
## [채점 결과](https://leetcode.com/problems/top-k-frequent-elements/submissions/1441610798)