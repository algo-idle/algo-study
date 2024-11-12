# 3. Longest Substring Without Repeating Characters

## 문제
Given a string s, find the length of the longest substring without repeating characters.


## 예제 입력 1
```text
s = "abcabcbb"
```
## 예제 출력 1
```text
3
```
## 예제 입력 2
```text
s = "bbbbb"
```
## 예제 출력 2
```text
1
```
## 예제 입력 3
```text
s = "pwwkew"
```
## 예제 출력 3
```text
3
```

## 코드
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left, right = 0, 0
        chars, result = set(), set()
        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
            else:
                chars.remove(s[left])
                left += 1
            result.add(right - left)
        return max(result)
```
### 코드 설명
변수 설명
- left: 부분 문자열의 시작 인덱스
- right: 부분 문자열의 끝 인덱스
- chars: 검사중인 부분 문자열에 존재하는 문자를 저장하기 위한 set
- result: 검사한 각 부분 문자열의 길이를 저장하기 위한 set

코드 설명
- left와 right를 0으로 설정 후 투포인터 시작.
- chars안에 right이 가리키는 문자가 없는 경우: chars에 추가 후 오른쪽 포인터를 한 칸 이동한다.
- chars안에 right이 가리키는 문자가 있는 경우: chars에서 삭제 후 왼쪽 포인터를 한 칸 이동한다.
- 부분 문자열 검사가 끝나면 해당 부분 문자열의 길이를 result에 추가한다.
- 문자열 끝까지 검사를 마친 후 result에서 가장 큰 값을 반환한다.

## [채점 결과](https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1449516580)