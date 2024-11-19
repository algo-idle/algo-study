from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        used_set = set()
        used = deque()

        res = []

        for _s in s:
            while _s in used_set:
                used_set.remove(used.popleft())

            used_set.add(_s)
            used.append(_s)

            res.append(len(used))

        return max(res)