class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result, resLen = "", float("inf")

        need, window = {}, {}
        for char in t:
            need[char] = 1 + need.get(char, 0)

        have = 0
        left = 0
        for right in range(len(s)):
            curr = s[right]
            window[curr] = 1 + window.get(curr, 0)

            if curr in need and window[curr] == need[curr]:
                have += 1

            while have == len(need):
                possible = s[left:right + 1]
                if len(possible) < resLen:
                    result = possible
                    resLen = len(possible)
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return result

# Time: O(n)
# Space: O(n + m)