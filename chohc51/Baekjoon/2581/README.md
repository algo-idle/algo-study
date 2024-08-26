# 2581번: 소수(브론즈 2)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  1초   | 128MB  |

## 문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
## 입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

## 출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

## 예제 입력 1
```text
60
100
```
## 예제 출력 1
```text
620
61
```

## 예제 입력 2
```text
64
65
```
## 예제 출력 2
```text
-1
```

## 코드
```python
min_num = int(input())
max_num = int(input())
target = -1
count = 0

for i in range(max_num,min_num-1,-1):
    if i == 1:
        continue
    if i == 2:
        target = i
        count += i
    for x in range(2,i):
        if i%x == 0:
            break
        if x == i-1:
            target = i
            count += i

if target == -1:
    print(target)
else:
    print(count)
    print(target)
    


        
```

## 채점 결과
![image](result.png)

## 스트릭
![image](streak.png)