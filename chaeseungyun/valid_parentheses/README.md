# valid_parentheses

## 문제
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
## 입력
```
s = "()"
```

## 출력
```
true
```
## 코드
```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        capacity = -1

        for item in s:
            if (item == '(' or item == '{' or item == '['):
                stack.append(item)
                capacity += 1
            if (item == ')' or item == '}' or item == ']'):
                if (capacity == -1):
                    return False
            if (item == ')'):
                capacity -= 1
                if (stack.pop() != '('):
                    return False
            if (item == '}'):
                capacity -= 1
                if (stack.pop() != '{'):
                    return False
            if (item == ']'):
                capacity -= 1
                if (stack.pop() != '['):
                    return False

        if (capacity != -1): return False
        return True
```

## 채점 결과
![alt text](image.png)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
leetcode 입니다