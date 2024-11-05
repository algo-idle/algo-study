class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        if nums[0] > 0 or nums[-1] < 0:
            return result
        for start in range(len(nums) - 2):
            if nums[start] > 0:
                break
            if start > 0 and nums[start - 1] == nums[start]:
                continue
            left, right = start + 1, len(nums) - 1
            while left < right:
                total = nums[start] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[start], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
