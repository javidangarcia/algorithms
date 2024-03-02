class Solution:
    def encode(self, strs):
        result = []
        for word in strs:
            result.append(str(len(word)) + "#" + word)
        return "".join(result)

    def decode(self, code):
        result = []
        i = 0
        while i < len(code):
            j = i
            while code[j] != "#":
                j += 1
            length = int(code[i:j])
            result.append(code[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result

# Time: O(n)
# Space: O(n)