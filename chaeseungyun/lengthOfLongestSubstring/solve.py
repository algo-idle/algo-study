class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        result = 0

        for i in range(len(s)):
            seen = set()
            progress = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                progress += 1
                result = max(result, progress)

        return result
