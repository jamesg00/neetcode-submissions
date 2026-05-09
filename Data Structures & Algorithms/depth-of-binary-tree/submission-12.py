# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #O(n) Time, O(h) Space
    #n is number of nodes in tree, h is height of tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Recursive DFS Approach

        #handles base case 
        if not root: return 0
        #recursive solution which deterines the maximum deth of tree, 
        #we add it by 1 because we incrememnt for eahc time we go deeper
        return 1 + max(self.maxDepth(root.left), 
        self.maxDepth(root.right))







        