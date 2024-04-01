# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            # calculates max path sum with split
            res = max(res, root.val + leftMax + rightMax)

            # calculates max path sum without split
            return root.val + max(leftMax, rightMax)
    
        res = float("-inf")
        dfs(root)
        return res

# Time: O(n)
# Space: O(h)