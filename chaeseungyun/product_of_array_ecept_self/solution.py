class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        up = [1] * len(nums)

        for i in range(len(nums) - 1):
            up[i + 1] = up[i] * nums[i]

        down = [1] * len(nums)

        for i in range(len(nums) - 1, 0, -1):
            down[i - 1] = down[i] * nums[i]

        result = []
        for x in zip(up, down):
            result.append(x[0] * x[1])
        
        return result
