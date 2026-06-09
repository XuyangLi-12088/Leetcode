# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # # Recrusion solution:
        # def helper(node1, node2):
        #     if node1 is None and node2 is None:
        #         return True

        #     if node1 is None or node2 is None:
        #         return False

        #     if node1.val != node2.val:
        #         return False

        #     return helper(node1.left, node2.right) and helper(node1.right, node2.left)

        # return helper(root.left, root.right)


        # 迭代法：
        if not root:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode:
                return False
            if leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left)
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
        return True

