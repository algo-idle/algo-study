# 1978번: 소수찾기 (브론즈 2)
|시간 제한|메모리 제한|
|:--:|:--:|
|2초|128MB|

## 문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

## 문제 설명
소수를 구하는 알고리즘을 알고 있어야함


## 입력
```
4
1 3 5 7
```

## 출력
```
3
```
## 코드
```
import math

N = int(input())
numbers = list(map(int, input().split()))

prime_count = 0

for n in numbers:
    if n <= 1:
        continue
    if n == 2:
        prime_count += 1
        continue
    if n % 2 == 0:
        continue
    is_prime = True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1

print(prime_count)

```

## 채점 결과
![image](https://github.com/BCSDLab/KOIN_OWNER_WEB/assets/112807899/5acaa44e-9b25-4fb7-a5c7-1e3e2558b42a)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
