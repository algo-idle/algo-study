# 44ms 99.06%
class Solution:
    def twoSum(self, nums, target):
        buf = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            try:
                idx = buf[target - nums[i]]
                if idx != i:
                    return [i, idx]
            except:
                pass
