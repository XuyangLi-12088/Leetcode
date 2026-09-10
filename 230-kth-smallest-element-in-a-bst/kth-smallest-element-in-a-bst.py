# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        def dfs(node):
            nonlocal i
            if node == None:
                return -1
            left_res = dfs(node.left)
            if left_res != -1:
                return left_res
            i += 1
            if i == k:
                return node.val
            return dfs(node.right)

        return dfs(root)
