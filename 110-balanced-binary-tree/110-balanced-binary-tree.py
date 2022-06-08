# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalancedHelper(self,root):
        
        if root is None:
            return [True,0]
            
        leftDiff , left = self.isBalancedHelper(root.left)
        rightDiff , right = self.isBalancedHelper(root.right)
        
        diff = abs(left - right)
        
        return [diff <= 1 and leftDiff and rightDiff, max(left,right) + 1]
    
    def isBalanced(self, root):
        
        return self.isBalancedHelper(root)[0]
        
        
        