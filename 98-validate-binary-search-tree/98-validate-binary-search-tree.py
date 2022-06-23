# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Inorder list of every valid BST is a sorted list
        
        inorderList = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            inorderList.append(node.val)
            inorder(node.right)
        inorder(root)
        for i in range(len(inorderList)-1):
            if inorderList[i] >= inorderList[i+1]:
                return False
        return True
        
        
#         def isValid(node,isLeft):
#             if node is None:
#                 return True
            
#             testVal = min(testVal,node.val) if isLeft else max(testVal,node.val)
                
#             isLeftValid = node.val > node.left.val if node.left else True
#             isRightValid = node.val < node.right.val if node.right else True
#             isRootValid = node.val < root.val if isLeft else node.val > root.val
#             isTreeValid = node.val < testVal if isLeft else node.val > testVal
#             isNodeValid = isLeftValid and isRootValid and isRightValid
            
#             return isNodeValid and isValid(node.left,isLeft) and isValid(node.right,isLeft)
        
        
#         return isValid(root.left,True) and isValid(root.right,False)
        