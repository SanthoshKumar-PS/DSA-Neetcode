# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        def dfs(root):
            if not root:
                return True
            left = dfs(root.left)
            if self.prev is not None and self.prev.val>=root.val:
                return False
            self.prev = root
            right = dfs(root.right)

            return left and right

        return dfs(root)