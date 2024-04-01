# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def preorder(root):
            nonlocal res
            if not root:
                res.append("null")
                return
            
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        res = []
        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        data = data.split(",")
        def construct():
            nonlocal index
            index += 1
            if index >= len(data) or data[index] == "null":
                return None
            
            root = TreeNode(int(data[index]))
            root.left = construct()
            root.right = construct()

            return root

        index = -1
        return construct()

# Time: O(n)
# Space: O(h)