# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        def height(node):
            
            if node is None:
                return [0,0]
            
            left,maxValL = height(node.left)
            right,maxValR = height(node.right)
            maxDia = max(maxValL,maxValR,left+right+1)
            return [max(left,right)+1,maxDia]
        
        numberOfNodesInDiameter = height(root)[1]
        
        # Note: We need to subtract '1' because it is asking length of path
        return numberOfNodesInDiameter - 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def findDiameter(node,level):
            
#             if node is None:
#                 return [level,level]
            
#             leftMax,leftMin = findDiameter(node.left,level-1 if node.left else level)
#             rightMax,rightMin = findDiameter(node.right,level+1 if node.right else level)
            
            
#             return [max(leftMax,rightMax),min(leftMin,rightMin)]
        
        
#         left,right = findDiameter(root,0)
#         # print(left)
#         # print(right)
#         return abs(left) + abs(right)