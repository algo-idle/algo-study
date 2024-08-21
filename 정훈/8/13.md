# 9012번: 괄호 (실버 4)
|시간 제한|메모리 제한|
|:--:|:--:|
|1초|128MB|

## 문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
## 문제 설명
전형적인 스택문제 스택을 구현해도 되지만, 파이썬의 list를 이용해서 풀어봄
그냥 하나하나 플래그를 둬서 해도 될듯?



## 입력
```
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
```

## 출력
```
NO
NO
YES
NO
YES
NO
```
## 코드
```
N = int(input())

for _ in range(N):
    S = input()
    st = []
    R = True
    
    for char in S:
        if char == '(':
            st.append(char)
        elif char == ')':
            if st:
                st.pop()
            else:
                R = False
                break
    
    if R and not st:
        print("YES")
    else:
        print("NO")

```

## 채점 결과
<img width="1187" alt="image" src="https://github.com/user-attachments/assets/0ba9b238-b5a5-4289-94aa-17993ca3a463">


## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
