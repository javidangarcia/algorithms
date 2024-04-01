class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index] or (row, col) in visited:
                return False

            visited.add((row, col))
            res = (dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1))
            visited.remove((row, col))

            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        
        return False

# Time: O(4^n)
# Space: O(n)