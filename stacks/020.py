class Solution:
    def isValid(self, s: str) -> bool:
        parens = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char not in parens:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != parens[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0

# Time: O(n)
# Space: O(n)