class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        rows = m
        cols = n
        
        # base case
        dp[1][1] = 1
        
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                if r==1 and c==1: continue
                    
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        return dp[m][n]