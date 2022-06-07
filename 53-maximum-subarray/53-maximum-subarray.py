class Solution(object):
    def maxSubArray(self, nums):
        
        
        maxSum = -sys.maxsize
        rollingSum = -sys.maxsize
        
        for num in nums:
            rollingSum += num
            # There will be a point where currSum has to be reset
            # and baggage of negative numbers needs to be dropped
            rollingSum = max(num,rollingSum)
            maxSum = max(maxSum,rollingSum)
            
            
        return maxSum
                
        