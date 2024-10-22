# 20. Valid Parentheses

## 문제
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## 예제 입력 1
```text
()
```
## 예제 출력 1
```text
True
```
## 예제 입력 2
```text
()[]{}
```
## 예제 출력 2
```text
True
```
## 예제 입력 3
```text
(]
```
## 예제 출력 3
```text
False
```
## 예제 입력 4
```text
([])
```
## 예제 출력 4
```text
True
```

## 코드
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for i in s:
            if i in parentheses:
                stack.append(parentheses[i])
            else:
                if not stack or stack.pop() != i:
                    return False
        return False if stack else True
```
### 코드 설명
- 문자열의 다음 괄호가 열림 괄호인 경우 stack 에 추가한다.
- 닫힘 괄호인 경우 스택이 비어있는지(= 열림 괄호 없이 닫힘 괄호가 출현), 스택에서 꺼낸 괄호와 쌍을 이루는지 검사
- 문자열을 모두 순회 후 stack이 비어져 있다면 True, 그렇지 않으면 Flase.

## [채점 결과](https://leetcode.com/problems/valid-parentheses/submissions/1430168197)