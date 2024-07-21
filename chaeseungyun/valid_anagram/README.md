# Two Sum

## 문제
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
## 입력
```
s = "anagram", t = "nagaram"
```

## 출력
```
true

```
## 코드
```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictOfS= {}
        dictOfT = {}

        if (len(s) != len(t)): return False

        for item in s:
            if (item in dictOfS): dictOfS[item] += 1
            else: dictOfS[item] = 1

        for item in t:
            if (dictOfS.get(item) == None): return False
            if (item in dictOfT): dictOfT[item] += 1
            else: dictOfT[item] = 1

        keyOfT = list(dictOfT.keys())

        for item in keyOfT:
            if (dictOfS.get(item) == None): return False
            if (dictOfS[item] != dictOfT[item]): return False

        
        return True
        
```

## 채점 결과
![alt text](image.png)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
leetcode 입니다