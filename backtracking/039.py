class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr, index, total):
            if index >= len(candidates) or total > target:
                return
            if total == target:
                res.append(curr.copy())
                return
            
            curr.append(candidates[index])
            dfs(curr, index, total + candidates[index])
            curr.pop()
            dfs(curr, index + 1, total)
        
        dfs([], 0, 0)
        return res

# Time: O(2^n)
# Space: O(n)