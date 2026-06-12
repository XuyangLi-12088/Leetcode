# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        count = 0
        def dfs(node: Optional[TreeNode], k: int):
            if node is None:
                return
            dfs(node.left, k)
            nonlocal ans, count
            count += 1
            if count == k:
                ans = node.val
            dfs(node.right, k)

        dfs(root, k)
        return ans