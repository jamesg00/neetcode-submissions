"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #base case

        if not node: return None

        #init hashmap
        mapp = {}

        #go through each node in graph using dfs

        def dfs(curr_node):

            if curr_node in mapp:
                return mapp[curr_node]

            
            #we create the clone
            clone = Node(curr_node.val)
            mapp[curr_node] = clone

            #go thru the neighbors

            for nei in curr_node.neighbors:
                clone_nei = dfs(nei)
                clone.neighbors.append(clone_nei)
            
            return clone
        
        return dfs(node)





