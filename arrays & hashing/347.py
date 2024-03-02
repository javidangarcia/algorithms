class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        freqArray = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        for num, freq in freqMap.items():
            freqArray[freq].append(num)
        
        result = []
        for i in range(len(freqArray) - 1, 0, -1):
            for num in freqArray[i]:
                result.append(num)
                if len(result) == k:
                    return result

# Time: O(n)
# Space: O(n)