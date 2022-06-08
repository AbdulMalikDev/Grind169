class Solution(object):
    def majorityElement(self, nums):
        
        runningCount = 1
        maxNum = nums[0]
        
        for i in range(1,len(nums)):
            num = nums[i]
            
            if num != maxNum:
                runningCount -= 1
                if runningCount == 0:
                    maxNum = num
                    runningCount = 1
                    
            else:
                runningCount += 1
                
        return maxNum
        
        