# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # BFS
        if not root:
            return ""

        output = []
        queue = collections.deque([root])
        while queue:
            pop = queue.popleft()
            if pop:
                output.append(str(pop.val))
                queue.append(pop.left)
                queue.append(pop.right)
            else:
                output.append("null")
        
        while output[-1] == "null":
            output.pop()
        print(output)
        return ",".join(output)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        node_list = data.split(",")
        root = TreeNode(int(node_list[0]))
        queue = collections.deque([root])
        i = 1

        while queue and i < len(node_list):
            node = queue.popleft()

            if i < len(node_list) and node_list[i] != "null":
                node.left = TreeNode(int(node_list[i]))
                queue.append(node.left)
            i += 1

            if i < len(node_list) and node_list[i] != "null":
                node.right = TreeNode(int(node_list[i]))
                queue.append(node.right)
            i += 1

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))