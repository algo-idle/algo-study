# 62ms 53.81%
class Solution:
    def twoSum(self, nums, target):
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort(key=lambda x: x[0])
        a, b = 0, len(nums) - 1
        while a < b:
            if nums[a][0] + nums[b][0] == target:
                break
            elif nums[a][0] + nums[b][0] < target:
                a += 1
            elif nums[a][0] + nums[b][0] > target:
                b -= 1
        a, b = nums[a][1], nums[b][1]
        if a > b:
            a, b = b, a
        return [a, b]
