# 70. Climbing Stairs

## 문제
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## 예제 입력 1
```text
n = 2
```
## 예제 출력 1
```text
2
```
## 예제 입력 2
```text
n = 3
```
## 예제 출력 2
```text
3
```


## 코드
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        curr = 1
        for i in range(n-1):
            curr = first + second
            first = second
            second = curr
        return curr
```
### 코드 설명
- 초기값 설정 후 해당 목표까지 값을 더해 정답을 구했다.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1, 1]
        for i in range(2, n+1):
            memo.append(memo[i-2] + memo[i-1])
        return memo[n]
```
### 코드 설명
- 초기 배열 설정 후 앞의 두 값을 더한 값을 배열에 추가하며 계산했다.
## [채점 결과](https://leetcode.com/problems/climbing-stairs/submissions/1436051917)