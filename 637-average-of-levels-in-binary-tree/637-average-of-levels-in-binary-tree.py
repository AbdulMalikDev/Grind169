# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque([root])
        result = []
        while queue:
            currentLevel = []
            for _ in range(len(queue)):
                
                node = queue.popleft()
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(sum(currentLevel)/len(currentLevel))
            
        return result
                    
            
                    
                
        