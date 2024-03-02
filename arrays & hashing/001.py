class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in indexMap:
                return [indexMap[diff], index]
            else:
                indexMap[num] = index
# Time: O(n)
# Space: O(n)