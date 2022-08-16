class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        smallToLeft = [0]*len(heights)
        smallToRight = [0]*len(heights)
        maxArea = -sys.maxsize
        stack = []
        
        for i in range(len(heights)):
            currentHeight = heights[i]
            
            if not stack:
                smallToLeft[i] = 0
                
            else:
                while stack and heights[stack[-1]] >= currentHeight:
                    stack.pop()        
                smallToLeft[i] = (stack[-1]+1) if stack else 0
                
            stack.append(i)
            
        stack = []
        
        for i in reversed(range(len(heights))):
            currentHeight = heights[i]
            
            if not stack:
                smallToRight[i] = len(heights)-1
            else:
                
                while stack and heights[stack[-1]] >= currentHeight:
                    stack.pop()
                smallToRight[i] = (stack[-1]-1) if stack else len(heights)-1
                
            stack.append(i)
            
        for i in range(len(heights)):
            maxArea = max(maxArea,heights[i] * (smallToRight[i] - smallToLeft[i] + 1))
            
        return maxArea
                
            
                
            
            
            
        