# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        #bfs approach
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            tree_level = []

            for i in range(len(q)):

                node = q.popleft()

                if node:
                    tree_level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            #make sure level is non empty
            if tree_level:
                res.append(tree_level)
        
        return res 




