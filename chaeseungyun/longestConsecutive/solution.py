class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## 파이썬 정렬함수 n log n
        if len(nums) == 0:
            return 0
        nums.sort()
        h = 1
        result = 1
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                h += 1
            elif nums[i+1] - nums[i] == 0:
                continue
            else:
                result = max(h, result)
                h = 1
        result = max(h, result)
        return result
