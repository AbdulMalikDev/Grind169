class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        memo = defaultdict(int)
        
        def minPath(r,c):
            
            if not 0<=r<rows or not 0<=c<cols:
                return sys.maxsize
            if r == rows-1 and c == cols-1:
                return grid[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = min(minPath(r+1,c),minPath(r,c+1)) + grid[r][c] 
            return memo[(r,c)]
        
        
        
        return minPath(0,0)
        
        