# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        # The intuition is bascially left left left then right right right then print
        result = []
        stack = []
        currNode = root
        
        while currNode or stack:
            
            # Go full left
            if currNode is not None:
                stack.append(currNode)
                currNode = currNode.left
                
            else:
                
                # Slight right
                temp = stack[-1].right
                
                # Yeah so there are no right nodes, so print post order stuff
                if not temp:
                    temp =  stack.pop()
                    result.append(temp.val)
                    
                    # Since we came here by doing a lot of right turns we don't want
                    # to end here again, so backtrack through all the right turns we took
                    while stack and stack[-1].right == temp:
                        temp = stack.pop()
                        result.append(temp.val)
                
                else:
                    # Keep going right 
                    currNode = temp
                    
                    
        return result
                    
                    
                    
                    
        