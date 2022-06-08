# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, node):
        
        if node is None:
            return 0

        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        
        return max(left,right)+1
        