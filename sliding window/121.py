class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        left, right = 0, 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            result = max(result, profit)
            if prices[left] > prices[right]:
                left = right
            right += 1
        return result

# Time: O(n)
# Space: O(1)