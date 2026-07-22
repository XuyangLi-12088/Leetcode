# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # Recursion Solution:
        # levels = []
        # if root is None:
        #     return levels

        # def helper(node, level):
        #     # start the current level
        #     if len(levels) == level:
        #         levels.append([])

        #     # append the current node value
        #     levels[level].append(node.val)

        #     # process child nodes for the next level
        #     if node.left:
        #         helper(node.left, level + 1)
        #     if node.right:
        #         helper(node.right, level + 1)

        # helper(root, 0)

        # return levels


        # # Queue Solution:
        # if not root:
        #     return []
        # queue = deque()
        # queue.append(root)
        # result = []
        # while queue:
        #     level = []
        #     cur_queue_size = len(queue)
        #     for _ in range(cur_queue_size):
        #         cur = queue.popleft()
        #         level.append(cur.val)
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        #     result.append(level)
                
        # return result


        # BFS:
        output = []
        if root:
            queue = collections.deque()
            queue.append(root)
            while queue:
                queue_size = len(queue)
                cur_level = []
                for _ in range(queue_size):
                    pop = queue.popleft()
                    cur_level.append(pop.val)
                    if pop.left:
                        queue.append(pop.left)
                    if pop.right:
                        queue.append(pop.right)
                output.append(cur_level)

        return output





