# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Helper(object):
    def __init__(self,difference,height):
        self.difference = difference
        self.height = height
        
class Solution(object):
    def isBalancedHelper(self,root):
        
        if root is None:
            return Helper(True,0)
            
        leftHelper = self.isBalancedHelper(root.left)
        rightHelper = self.isBalancedHelper(root.right)
        
        diff = abs(leftHelper.height - rightHelper.height)
        
        return Helper(diff <= 1 and leftHelper.difference and rightHelper.difference,max(leftHelper.height,rightHelper.height) + 1)
        # return [, ]
    
    def isBalanced(self, root):
        
        return self.isBalancedHelper(root).difference
        
        
        