from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        
        for word in strs:
            charArray = [0] * 26
            for char in word:
                charArray[ord(char) - ord("a")] += 1
            anagramMap[tuple(charArray)].append(word)

        return anagramMap.values()

# Time: O(n * m)
# Space: O(n)