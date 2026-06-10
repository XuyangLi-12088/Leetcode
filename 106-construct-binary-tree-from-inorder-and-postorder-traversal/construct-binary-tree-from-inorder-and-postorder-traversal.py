# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # if not postorder:   # 空节点
        #     return None
        # left_size = inorder.index(postorder[-1])   # 左子树的大小
        # left = self.buildTree(inorder[:left_size], postorder[:left_size])
        # right = self.buildTree(inorder[left_size + 1:], postorder[left_size:-1])
        # return TreeNode(postorder[-1], left, right)

        index = {x: i for i, x in enumerate(inorder)}

        def dfs(in_l: int, post_l: int, post_r: int) -> Optional[TreeNode]:
            if post_l == post_r:    # 空节点
                return None
            left_size = index[postorder[post_r - 1]] - in_l    # 左子树的大小
            left = dfs(in_l, post_l, post_l + left_size)
            right = dfs(in_l + left_size + 1, post_l + left_size, post_r - 1)
            return TreeNode(postorder[post_r - 1], left, right)

        return dfs(0, 0, len(postorder))