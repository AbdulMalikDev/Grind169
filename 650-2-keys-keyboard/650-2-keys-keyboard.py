class Solution:
    def minSteps(self, n: int) -> int:
        
        @lru_cache(None)
        def minStep(num,copied):
            
            if num == n:
                return 0
            if num > n:
                return sys.maxsize
            
            # choice1 first copyAll and paste
            result1 = minStep(num + num,num) + 2
            # choice 2 Paste
            if copied == 0:
                return result1
            result2 = minStep(num + copied,copied) + 1
            
            return min(result1,result2)
        
        
        return minStep(1,0)
        
        
        
        