# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        i = 0
        def dfs(node):
            nonlocal i, ans
            if node == None:
                return
            dfs(node.left)
            i += 1
            if i == k:
                ans = node.val
            dfs(node.right)
            return

        dfs(root)
        return ans