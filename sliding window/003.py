class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            else:
                charSet.add(s[right])
                result = max(result, right - left + 1)
                right += 1
        return result

# Time: O(n)
# Space: O(n)