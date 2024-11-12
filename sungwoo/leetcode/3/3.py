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