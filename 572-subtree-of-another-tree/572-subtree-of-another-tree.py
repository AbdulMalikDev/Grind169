# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkIfSameSubtree(self,node,subroot):
        
        if node == None and subroot == None:
            return True
        
        elif node == None or subroot == None:
            return False
        
        elif node.val != subroot.val:
            return False
        
        # result = False
        result = self.checkIfSameSubtree(node.left,subroot.left)
        result = self.checkIfSameSubtree(node.right,subroot.right) and result
        
        return result
        
        
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def traverseRoot(node):
            if node == None:
                return False
            
            result = self.checkIfSameSubtree(node,subRoot)
            
            result = traverseRoot(node.left) or result
            result = traverseRoot(node.right) or result
            
            return result
        
        return traverseRoot(root)
            
            
        