# Two Sum

## 문제
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
## 입력
```
s = "A man, a plan, a canal: Panama"
```

## 출력
```
true
"amanaplanacanalpanama" is a palindrome.
```
## 코드
```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s.replace(" ",'')) == 0 or len(s) == 1): return True

        alphanumeric = []

        for char in s:
            if ((ord(char) >= 48 and ord(char) <= 57)):
                alphanumeric.append(char)
                continue
            if ((ord(char) >= 65 and ord(char) <= 90)):
                alphanumeric.append(char.lower())
                continue
            if ((ord(char) >= 97 and ord(char) <= 122)):
                alphanumeric.append(char)

        if len(alphanumeric) == 0: return True
        
        length = len(alphanumeric)
        for i in range(length):
            if (i > length // 2): break
            if (alphanumeric[i] != alphanumeric[length - i - 1]): return False
        
```

## 채점 결과
![alt text](image.png)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
leetcode 입니다