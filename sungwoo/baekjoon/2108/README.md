# 2108번: 통계학(실버 3)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  2초   | 256MB  |

## 문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값 
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값 
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

## 출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

## 예제 입력 1
```text
5
1
3
8
-2
2
```
## 예제 출력 1
```text
2
2
1
10
```
## 예제 입력 2
```text
1
4000
```
## 예제 출력 2
```text
4000
4000
4000
0
```
## 예제 입력 3
```text
5
-1
-2
-3
-1
-2
```
## 예제 출력 3
```text
-2
-2
-1
2
```
## 예제 입력 4
```text
3
0
0
-1
```
## 예제 출력 4
```text
0
0
0
1
```

## 코드
```python
import sys
import math
from collections import Counter
read = sys.stdin.readline

N = int(read())
nums = [int(read()) for _ in range(N)]
result = [math.floor(sum(nums) / N + 0.5)]

nums.sort()
result.append(nums[math.floor(N/2)])

if len(nums) == 1:
    result.append(nums[0])
else:
    memo = Counter(nums).most_common(2)
    result.append(memo[1][0] if memo[0][1] == memo[1][1] else memo[0][0])

result.append(nums[-1] - nums[0])

print(*result, sep='\n')
```

## 채점 결과
![image](result_img.png)

## 스트릭
![image](streak_img.png)