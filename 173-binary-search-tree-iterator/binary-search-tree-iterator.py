# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.queue = deque()
    #     self.inOrder(root)

    # def inOrder(self, root):
    #     if not root:
    #         return
    #     self.inOrder(root.left)
    #     self.queue.append(root.val)
    #     self.inOrder(root.right)

    # def next(self) -> int:
    #     return self.queue.popleft()

    # def hasNext(self) -> bool:
    #     if len(self.queue) > 0:
    #         return True
    #     else:
    #         return False


    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()