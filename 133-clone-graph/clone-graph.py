"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS:
        if not node:
            return None

        hash_map = {}
        queue = collections.deque()
        queue.append(node)
        hash_map[node.val] = Node(node.val, [])
        while queue:
            pop = queue.popleft()
            pop_node = hash_map[pop.val]
            for n in pop.neighbors:
                if n.val not in hash_map:
                    hash_map[n.val] = Node(n.val, [])
                    queue.append(n)
                pop_node.neighbors.append(hash_map[n.val])

        return hash_map[node.val]
        
        