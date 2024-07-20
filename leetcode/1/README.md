# 1. Two Sum

## 문제
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## 예제 입력 1
```text
nums = [2,7,11,15], target = 9
```
## 예제 출력 1
```text
[0,1]
```
## 예제 입력 2
```text
nums = [3,2,4], target = 6
```
## 예제 출력 2
```text
[1,2]
```
## 예제 입력 3
```text
nums = [3,3], target = 6
```
## 예제 출력 3
```text
[0,1]
```

## 코드
```python
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        fp = 0
        bp = len(nums) - 1
        sortedList = sorted(nums)
        while True:
            if sortedList[fp] + sortedList[bp] < target:
                fp += 1
            elif sortedList[fp] + sortedList[bp] > target:
                bp -= 1
            else:
                break
        result = []
        result.append(nums.index(sortedList[fp]))
        result.append(len(nums) - nums[-1::-1].index(sortedList[bp]) - 1)
        return(result)
```
### 코드 설명
**정답이 무조건 존재하고 하나만 있다는 조건을 보고 투포인터 사용**

- 투포인터를 통해 정답을 찾기 위해선 리스트 정렬을 해야하는데 정렬하면 기존 리스트에서의 인덱스를 못찾기 때문에 정렬된 새로운 리스트를 활용함
- 반복문을 통해 두 포인터에 존재하는 값을 더해 찾는 값보다 작으면 앞의 포인터를 한칸 뒤로, 찾는 값보다 크면 뒤의 포인터를 한칸 앞으로 옮겨가며 탐색
정답을 찾으면 탐색 중단
- 원본 리스트에서의 인덱스 반환

시간 복잡도는 잘 줄인 것 같은데 주어진 리스트만한 크기의 리스트를 추가로 생성하고 결과를 반환할 때도 새로운 리스트를 생성하는 등 공간복잡도 면에 있어선 조금 아쉽다.



## 채점 결과
![image](result_img.png)
