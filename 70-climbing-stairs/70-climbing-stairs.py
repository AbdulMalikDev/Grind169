class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        # memoization
        # recording values of overlapping recursive calls
        # decreases the complexity
        
        # top down
#         memo = defaultdict(int)
#         def stairs(n):
            
#             if n in memo:
#                 return memo[n]
            
#             if n == 0:
#                 return 1
#             elif n < 0:
#                 return 0
            
#             memo[n-1] = stairs(n-1)
#             memo[n-2] = stairs(n-2)
            
#             return memo[n-1] + memo[n-2]
        
#         return stairs(n)


        # bottom up
        dp = [0] * (n+1)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]
        
        
        