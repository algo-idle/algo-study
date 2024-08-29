# 11050번: 이항 계수 1(브론즈 1)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  1초   | 256MB  |

## 문제
자연수 N과 정수 K가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N과 K가 주어진다.(1<= N <= 10, 0 <= K <= N)

## 출력
이항계수를 출력한다. 

## 예제 입력 1
```text
5 2
```
## 예제 출력 1
```text
10
```
## 코드
```python
from sys import *

a,b = map(int,stdin.readline().split())
up = 1
down = 1
if (a//2)<b:
    b = a-b
for _ in range(b):
    up = up*a
    a -=1
for _ in range(b):
    down = down*b
    b-=1

print(up//down)
```

## 채점 결과
![image](result.png)

## 스트릭
![image](streak.png)