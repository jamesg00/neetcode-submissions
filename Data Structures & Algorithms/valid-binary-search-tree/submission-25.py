# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #is ths subtree rooted at node valid?
        def isValid(node, left, right):
            #base case
            if not node: return True

            #check current node against the bounds.
            #strictly greater than left, less than right
            if not (node.val > left and node.val < right):
                return False
            
            #recurse into left and right
            #left, all values must be greater than left, less than node.val
            #right, all values must be greater than node.val, less than right 
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)

        #pass params of our root, negative and positive infinity
        return isValid(root, float('-inf'), float('inf'))