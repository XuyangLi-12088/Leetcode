# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归法:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root) != -1:
            return True
        else:
            return False

    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.get_height(root.left)
        if left_height == -1:
            return -1
        right_height = self.get_height(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1