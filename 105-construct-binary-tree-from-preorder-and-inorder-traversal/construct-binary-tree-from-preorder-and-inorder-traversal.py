# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_dict = {n:i for i, n in enumerate(inorder)}

        def dfs(pre_l, pre_r, in_l):
            if pre_l == pre_r:
                return None
            left_size = in_dict[preorder[pre_l]] - in_l # 左子树的大小
            left = dfs(pre_l+1, pre_l+1+left_size, in_l)
            right = dfs(pre_l+1+left_size, pre_r, in_dict[preorder[pre_l]]+1)
            return TreeNode(preorder[pre_l], left, right)

        return dfs(0, len(preorder), 0)






        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0], None, None)
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        p = preorder[0]
        p_index = inorder.index(p)
        l_in = inorder[:p_index]
        r_in = inorder[p_index+1:]

        l_pre = preorder[1:1+len(l_in)]
        r_pre = preorder[1+len(l_in):]

        return TreeNode(p, self.buildTree(l_pre, l_in), self.buildTree(r_pre, r_in))
        

