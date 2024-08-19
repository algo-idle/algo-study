class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        fp = 0
        bp = len(nums) - 1
        sortedList = sorted(nums)
        while True:
            if sortedList[fp] + sortedList[bp] < target:
                fp += 1
            elif sortedList[fp] + sortedList[bp] > target:
                bp -= 1
            else:
                break
        result = []
        result.append(nums.index(sortedList[fp]))
        result.append(len(nums) - nums[-1::-1].index(sortedList[bp]) - 1)
        return(result)

s = Solution()
print(s.twoSum([2,7,11,15], 9))