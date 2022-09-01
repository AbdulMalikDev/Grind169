# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def recurse(root,maxNum):
            
            if root is None:
                return 0
            goodNodes = 0
            if root.val >= maxNum:
                goodNodes += 1
                maxNum = root.val 
            
            leftResult = recurse(root.left,maxNum)
            rightResult = recurse(root.right,maxNum)
            
            return goodNodes + leftResult + rightResult
        
        
        return recurse(root,-sys.maxsize)
        