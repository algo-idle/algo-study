# 11726번: 2xn 타일링(실버 3)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  1초   | 256MB  |

## 문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

<img alt="image" height="100" src="problem_img.png" width="200"/>


## 입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

## 출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

## 예제 입력 1
```text
2
```
## 예제 출력 1
```text
2
```

## 예제 입력 2
```text
9
```
## 예제 출력 2
```text
55
```

## 코드
```python
import sys
read = sys.stdin.readline

n = int(read())
memo = [1, 2]
for i in range(2, n):
    memo.append((memo[i-2] + memo[i-1]) % 10007)
print(memo[n-1])
```

## 채점 결과
![image](result_img.png)

## 스트릭
![image](streak_img.png)