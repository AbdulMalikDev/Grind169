# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkIfPalindrome(self,nums):
        return nums[:]==nums[::-1]
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        
        while queue:
            children = []
            for _ in range(len(queue)):
                node = queue.popleft()
                children.append(node.val)
                if node and node.val!=-101:
                    queue.append(node.left if node.left else TreeNode(-101))
                    queue.append(node.right if node.right else TreeNode(-101))
                
                    
            if not self.checkIfPalindrome(children):
                print(children)
                return False
            
        return True
                
            
            
        
        