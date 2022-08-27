# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeftBoundary(self,root):
        
        if root is None or (root.left is None and root.right is None):
            return []
        
        if root.left is None:
            return [root.val] + self.getLeftBoundary(root.right)
        
        return [root.val] + self.getLeftBoundary(root.left)
    
    def getRightBoundary(self,root):
        
        if root is None or (root.left is None and root.right is None):
            return []
        
        if root.right is None:
            return self.getRightBoundary(root.left) + [root.val] 
        
        return self.getRightBoundary(root.right) + [root.val]
    
    def getLeafNodes(self,root):
        if root is None:
            return []
        result = []
        result += self.getLeafNodes(root.left)
        if root.left is None and root.right is None:
            result += [root.val] 
        result += self.getLeafNodes(root.right)
        return result
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.boundary = [] if root.left is None and root.right is None else [root.val]
        self.boundary += self.getLeftBoundary(root.left)
        print(self.boundary)
        self.boundary += self.getLeafNodes(root)
        print(self.boundary)
        self.boundary += self.getRightBoundary(root.right)
        print(self.boundary)
        return self.boundary