# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # traverse both at same time
        # if any tree differs simply return false
        
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        elif p.val != q.val:
            return False
        
        leftResult = self.isSameTree(p.left,q.left)
        rightResult = self.isSameTree(p.right,q.right)
        
        return leftResult and rightResult
        