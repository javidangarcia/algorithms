class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)

        result = 0
        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                result = max(result, length)

        return result

# Time: O(n)
# Space: O(n)
