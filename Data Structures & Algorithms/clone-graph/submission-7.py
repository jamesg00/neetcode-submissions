"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        old_tracker = {}

        def dfs(node):

            if node in old_tracker:
                return old_tracker[node]

            copy = Node(node.val)
            old_tracker[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        
        return dfs(node) if node else None










        