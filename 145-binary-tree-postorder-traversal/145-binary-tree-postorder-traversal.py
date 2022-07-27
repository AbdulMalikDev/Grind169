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
        stack = [root]
        currNode = root
        
        while stack:
            
            if currNode is not None:
                if currNode!=root:
                    stack.append(currNode)
                currNode = currNode.left
                # for a in stack:
                #     print(a.val)
                # print("")
                
            else:
                
                temp = stack[-1].right
                
                if not temp:
                    temp =  stack.pop()
                    result.append(temp.val)
                    
                    while stack and stack[-1].right == temp:
                        temp = stack.pop()
                        result.append(temp.val)
                
                else:
                    currNode = temp
                    
                    
        return result
                    
                    
                    
                    
        