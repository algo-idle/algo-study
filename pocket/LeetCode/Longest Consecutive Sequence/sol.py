class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = list(set(nums))
        num_set = set(nums)
        nums.sort()

        res = 0
        curr = 1

        for n in nums:
            if n - 1 not in num_set:
                curr = 1
            else:
                res = max(res, curr + 1)
                curr += 1

        res = max(res, curr)

        return res
