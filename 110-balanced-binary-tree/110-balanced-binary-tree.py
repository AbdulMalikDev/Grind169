# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Note : It's always good to show off some OOPS skills
# specially when you're returning multiple values in recursion
# you want to return an object instead of a whole big list and then
# packing/unpacking list in each function.

class Helper(object):
    def __init__(self,isDiffValid,height):
        self.isDiffValid = isDiffValid
        self.height = height
        
class Solution(object):
    def isBalancedHelper(self,root):
        
        if root is None:
            return Helper(True,0)
            
        leftHelper = self.isBalancedHelper(root.left)
        rightHelper = self.isBalancedHelper(root.right)
        
        diff = abs(leftHelper.height - rightHelper.height)
        
        isValidNode = diff<=1 and leftHelper.isDiffValid and rightHelper.isDiffValid
        return Helper( isValidNode, max(leftHelper.height,rightHelper.height) + 1)
    
    def isBalanced(self, root):
        return self.isBalancedHelper(root).isDiffValid
        
        
        