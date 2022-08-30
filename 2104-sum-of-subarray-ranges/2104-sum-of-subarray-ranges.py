class Solution:
    def getMin(self,nums):
        stack = []
        result = [0] * len(nums)
        previousLess = [-1] *  len(nums)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
                
            if stack:
                previousLess[i] = stack[-1]
            
            stack.append(i)
        
        for i in range(len(nums)):
            result[i] = result[previousLess[i]] + (i - previousLess[i])*nums[i]
            
        return sum(result)
    
    def getMax(self,nums):
        stack = []
        result = [0] * len(nums)
        previousLess = [-1] *  len(nums)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
                
            if stack:
                previousLess[i] = stack[-1]
            
            stack.append(i)
        
        for i in range(len(nums)):
            result[i] = result[previousLess[i]] + (i - previousLess[i])*nums[i]
            
        return sum(result)
            
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.getMax(nums) - self.getMin(nums)
        
        