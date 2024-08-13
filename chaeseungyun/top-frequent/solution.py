class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sortedList = sorted(freq, key=lambda num: freq[num])
        return sortedList[-k:]