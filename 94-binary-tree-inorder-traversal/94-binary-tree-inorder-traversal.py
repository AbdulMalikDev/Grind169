# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Basically full left left, print, then right right
        
        stack = []
        currNode = root
        result = []
        
        while currNode or stack:
            
            # Going full left left
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
                
            currNode = stack.pop()
            result.append(currNode.val)
            currNode = currNode.right
            
#             arr = []
#             while currNode:
#                 arr.append(currNode)
#                 currNode = currNode.right
            
#             if arr:
#                 arr = arr[::-1]
#                 for a in arr:
#                     stack.append(a)
                
                
        return result
            
            
        