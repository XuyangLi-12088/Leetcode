# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def checkBST(root, min_val, max_val):
            if not root:
                return True

            if min_val < root.val < max_val:
                l = checkBST(root.left, min_val, root.val)
                r = checkBST(root.right, root.val, max_val)
                return l & r
            else:
                return False

        return checkBST(root, -inf, inf)

    # def isValidBST(self, root: Optional[TreeNode], left = -inf, right = inf) -> bool:
    #     if root == None:
    #         return True
    #     x = root.val
    #     return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)




        