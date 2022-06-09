class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = defaultdict(int)
        def stairs(n):
            
            if n in memo:
                return memo[n]
            
            if n == 0:
                return 1
            elif n < 0:
                return 0
            
            memo[n-1] = stairs(n-1)
            memo[n-2] = stairs(n-2)
            
            return memo[n-1] + memo[n-2]
        
        return stairs(n)
        
        
        