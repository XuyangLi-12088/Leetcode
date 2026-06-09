# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return False

    #     def helper(root, min_val, max_val):
    #         if (root.val > min_val and root.val < max_val):
    #             if root.left and root.right:
    #                 return helper(root.left, min_val, root.val) and helper(root.right, root.val, max_val)
    #             elif root.left:
    #                 return helper(root.left, min_val, root.val)
    #             elif root.right:
    #                 return helper(root.right, root.val, max_val)
    #             else:
    #                 return True
    #         else:
    #             return False
            
    #     return helper(root, float('-inf'), float('inf'))

    def isValidBST(self, root: Optional[TreeNode], left = -inf, right = inf) -> bool:
        if root == None:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)




        