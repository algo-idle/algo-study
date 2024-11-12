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
                result.add(right - left)
        return max(result)
