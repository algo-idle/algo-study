from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
        sorted_list = sorted(dict.items(), key=lambda x:x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_list[i][0])
        return result