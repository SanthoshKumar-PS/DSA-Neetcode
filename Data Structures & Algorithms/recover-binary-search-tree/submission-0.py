# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.prev = None
        self.first, self.second = None, None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.prev is not None and self.prev.val>root.val:
                if self.first is None:
                    self.first = self.prev
                self.second = root
            self.prev = root
            dfs(root.right)

        dfs(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val