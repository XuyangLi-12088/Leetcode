# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # Recursion Solution:
        # if root is None:
        #     return 0
        # else:
        #     left = self.maxDepth(root.left)
        #     right = self.maxDepth(root.right)
        #     return max(left, right) + 1

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        

        # # BFS Solution:
        # if not root:
        #     return 0
        # queue = deque()
        # queue.append(root)
        # result = 0
        # while queue:
        #     cur_queue_size = len(queue)
        #     for _ in range(cur_queue_size):
        #         cur = queue.popleft()
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        #     result += 1
        # return result
        