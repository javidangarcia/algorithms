class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = float("-inf")
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return result

# Time: O(n)
# Space: O(1)