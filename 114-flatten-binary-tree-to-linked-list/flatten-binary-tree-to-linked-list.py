# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    head = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 头插法
        # # 右 - 左 - 根
        # self.flatten(root.right)
        # self.flatten(root.left)
        # root.left = None
        # root.right = self.head  # 头插法，相当于链表的 root.next = head
        # self.head = root    # 现在链表头节点是 root

        # 分治
        if root is None:
            return None
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)
        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        return right_tail or left_tail or root