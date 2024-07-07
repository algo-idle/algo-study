# 1978번: 소수찾기 (브론즈 2)
|시간 제한|메모리 제한|
|:--:|:--:|
|2초|128MB|

## 문제


## 문제 설명
층마다 갯수를 생각해서 해당 층의 마지막 번호 범위내에 있으면 그 층수 만큼 이동거리
![image](https://github.com/hoooooony/gomars/assets/112807899/0375eb33-95e9-4884-90ce-915c1ce6efba)


## 입력
```
13
```

## 출력
```
3
```
## 코드
```
def min_steps(N):
    if N == 1:
        return 1

    layer = 1
    max_number_in_layer = 1

    while N > max_number_in_layer:
        max_number_in_layer += 6 * layer
        layer += 1

    return layer


N = int(input())

print(min_steps(N))

```

## 채점 결과
![image](https://github.com/hoooooony/gomars/assets/112807899/8b028178-e95d-4f0a-b50b-e7ed5724709c)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
