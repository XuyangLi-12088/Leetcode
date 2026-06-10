# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder:    # 空节点
        #     return None
        # left_size = inorder.index(preorder[0])  # 左子树的大小
        # left = self.buildTree(preorder[1: 1 + left_size], inorder[:left_size])
        # right = self.buildTree(preorder[1 + left_size:], inorder[1 + left_size:])
        # return TreeNode(preorder[0], left, right)

        index = {x: i for i, x in enumerate(inorder)}

        # 根据 preorder[pre_l:pre_r] 和 inorder[in_l:in_r] 生成二叉树，其中 in_r 没用到，可以省略
        def dfs(pre_l: int, pre_r: int, in_l: int) -> Optional[TreeNode]:
            if pre_l == pre_r:  # 空节点
                return None
            left_size = index[preorder[pre_l]] - in_l
            left = dfs(pre_l + 1, pre_l + 1 + left_size, in_l)
            right = dfs(pre_l + 1 + left_size, pre_r, in_l + 1 + left_size)
            return TreeNode(preorder[pre_l], left, right)
            
        return dfs(0, len(preorder), 0) # 左闭右开区间