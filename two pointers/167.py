class Solution:
    def twoSumInputSorted(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else:
                return [left + 1, right + 1]

# Time: O(n)
# Space: O(1)