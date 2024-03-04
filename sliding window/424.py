class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            windowLen = right - left + 1
            mostFreqCount = max(count.values())
            if windowLen - mostFreqCount <= k:
                result = max(result, right - left + 1)
            else:
                count[s[left]] -= 1
                left += 1

        return result

# Time: O(n)
# Space: O(n)