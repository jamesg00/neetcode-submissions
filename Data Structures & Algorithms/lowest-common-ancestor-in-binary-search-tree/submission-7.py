# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #bst approach, recurison solution 
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root or not q or not p: return None

        #both ndoes are in the left subtree
        elif (max(p.val, q.val) < root.val):
            #move deeper inside left
            return self.lowestCommonAncestor(root.left, p, q)

        #both nodes are in the right subtree
        elif (min(p.val, q.val) > root.val):
            #move deeper inside right
            return self.lowestCommonAncestor(root.right, p, q)
        
        #return root when done 
        else:
            return root 


        






