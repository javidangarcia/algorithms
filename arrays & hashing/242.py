class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countMapS, countMapT = {}, {}
        
        for letter in s:
            countMapS[letter] = 1 + countMapS.get(letter, 0)

        for letter in t:
            countMapT[letter] = 1 + countMapT.get(letter, 0)

        return countMapS == countMapT

# Time: O(n + m)
# Space: O(n + m)