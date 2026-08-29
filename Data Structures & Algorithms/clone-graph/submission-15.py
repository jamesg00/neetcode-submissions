"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        mapp = {}

        def dfs(curr_node):
            
            if curr_node in mapp:
                return mapp[curr_node]
            
            clone = Node(curr_node.val)
            mapp[curr_node] = clone

            for nei in curr_node.neighbors:
                clone_nei = dfs(nei)
                clone.neighbors.append(clone_nei)
            
            return clone 

        return dfs(node)
     




