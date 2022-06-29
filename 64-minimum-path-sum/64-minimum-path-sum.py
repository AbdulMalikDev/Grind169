class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        # Tabulation
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        
        # base case
        for i in range(2,cols+1):
            dp[0][i] = sys.maxsize
        for j in range(2,rows+1):
            dp[j][0] = sys.maxsize
            
            
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                
                # 'grid[r-1][c-1]' because dp is 1-indexed
                dp[r][c] = min(dp[r-1][c],dp[r][c-1]) + grid[r-1][c-1]
                
        return dp[rows][cols]
        
        
        
#         Memoization
#         rows = len(grid)
#         cols = len(grid[0])
#         memo = defaultdict(int)
        
#         def minPath(r,c):
            
#             if not 0<=r<rows or not 0<=c<cols:
#                 return sys.maxsize
#             if r == rows-1 and c == cols-1:
#                 return grid[r][c]
#             if (r,c) in memo:
#                 return memo[(r,c)]
            
#             memo[(r,c)] = min(minPath(r+1,c),minPath(r,c+1)) + grid[r][c] 
#             return memo[(r,c)]
        
        
        
        return minPath(0,0)
        
        