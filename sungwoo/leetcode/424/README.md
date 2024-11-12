# 424. Longest Repeating Character Replacement

## 문제
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## 예제 입력 1
```text
s = "ABAB", k = 2
```
## 예제 출력 1
```text
4
```
## 예제 입력 2
```text
s = "AABABBA", k = 1
```
## 예제 출력 2
```text
4
```

## 코드
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == k:
            return k
        s_set = set(s)
        result = set()
        for char in s_set:
            left, right, count = 0, 0, 0
            while right < len(s):
                if s[right] == char:
                    right += 1
                elif count < k:
                    count += 1
                    right += 1
                elif s[left] == char:
                    left += 1
                else:
                    count -= 1
                    left += 1
                result.add(right-left)
        return max(result)
```
### 코드 설명
- 바꿀 수 있는 문자의 개수가 k개인 경우, 만들 수 있는 부분 문자열의 최대 길이는 이와 같으므로 바로 반환한다.
- s에 있는 문자의 종류만큼 탐색을 하게된다. = char
- 검사할 윈도우의 시작 인덱스인 left, 끝 인덱스인 right, 해당 윈도우에서 바꾼 문자의 수인 count를 조작하며 탐색이 진행된다.
- right를 먼저 조작하게 된다.
   - 윈도우의 끝값이 char와 같다면 윈도우의 크기를 한 칸 늘린다.
   - 윈도우의 끝값이 char와 다르고 바꾼 문자의 개수가 k보다 작으면, count를 증가시키고 윈도우의 크기를 한 칸 늘린다.
- 위 두가지 경우가 아니라면 left를 조작한다.
   - 윈도우의 시작값이 char와 같다면 윈도우의 크기를 한 칸 줄인다.
   - 윈도우의 시작값이 char와 다르다면 count를 감소시키고 윈도우의 크기를 한 칸 줄인다.
- 탐색을 진행하며 result에 윈도우의 크기를 저장한다.
- 가능한 윈도우의 크기 중 최대값을 반환한다.

## [채점 결과](https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1450551053)