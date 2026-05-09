# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #global tracker diameter
        diameter = 0

        
        def dfs(node):
            #base case
            if not node: return 0

            #how deep is my left subtree?
            l = dfs(node.left)
            #how deep is my right subtree?
            r = dfs(node.right)

            nonlocal diameter

            #update diameter with the longest path from each node
            diameter = max(diameter, l+r)

            #return depth of this node to the parent so it can
            #calculate its own l + r
            return 1 + max(l, r)
        dfs(root)

        return diameter

        
        