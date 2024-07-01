# 2557번: Hello World (실버 5)
|시간 제한|메모리 제한|
|:--:|:--:|
|2초|256MB|

## 문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

 1. 길이가 짧은 것부터
 2. 길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

## 문제 설명
파이썬 



## 입력
```
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
```

## 출력
```
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
```
## 코드
```
num = input()
arr = []
for i in range(int(num)):
    arr.append(input())

arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))

for i in range(len(arr)):
    print(arr[i])
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/112807899/e0fc84c3-3450-4a11-98d9-89bf342f63b5)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
