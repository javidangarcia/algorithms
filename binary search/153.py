class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        return min(result, nums[0])

# Time: O(log(n))
# Space: O(1)