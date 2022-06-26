class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        totalSum = sum(cardPoints)
        n = len(cardPoints)
        windowStart,runningSum,minSum = 0,0,sys.maxsize
        
        for windowEnd in range(len(cardPoints)):
            currNum = cardPoints[windowEnd]
            runningSum += currNum
            
            if windowEnd >= (n-k):
                runningSum -= cardPoints[windowStart]
                windowStart += 1
                
            if (windowEnd - windowStart + 1) == (n-k):
                print(windowStart,windowEnd)
                minSum = min(minSum,runningSum)
                
        return totalSum - minSum
                
            
            
        