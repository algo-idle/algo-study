class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        result = [1]
        prev, cursor = nums[0], 0
        for num in nums:
            if num == prev:
                continue
            elif num == prev + 1:
                result[cursor] += 1
            else:
                cursor += 1
                result.append(1)
            prev = num
        return max(result)