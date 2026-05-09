"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #O(n) = E+V
        
        #track visited nodes
        old_new_nodes = {}

        def dfs(node):
            #did we already clone the node?
            if node in old_new_nodes:
                #if yes return the existing
                #prevents infinite loops in cyclic graphs
                return old_new_nodes[node]
            
            #brand new node with teh same value
            copy = Node(node.val)
            #map the frequency to the copy
            old_new_nodes[node] = copy

            #loop through adjacent nodes
            for n in node.neighbors:
                #clone neighbor and attach the cloned neighbor
                #to the cloned node
                copy.neighbors.append(dfs(n))

            #return fully constructued node
            return copy

        return dfs(node) if node else None





        