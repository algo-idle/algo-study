# 2869번: 달팽이는 올라가고 싶다(브론즈 1)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  0.25초   | 128MB  |

## 문제
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

## 출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

## 예제 입력 1
```text
2 1 5
```
## 예제 출력 1
```text
4
```

## 예제 입력 2
```text
5 1 6
```
## 예제 출력 2
```text
2
```


## 예제 입력 3
```text
100 99 1000000000
```
## 예제 출력 3
```text
999999901
```


## 코드
```python
from sys import *
import math
climb,slip,end = map(int,stdin.readline().split())
count = 1
if climb>=end:
    print(count)
else: #climb +(climb-slip)*n >= end에서 n이 일수(첫 climb는 1로 카운트)
    n = math.ceil((end-climb)/(climb-slip))
    count+= n
    print(count)


        
```

## 채점 결과
![image](result.png)

## 스트릭
![image](streak.png)