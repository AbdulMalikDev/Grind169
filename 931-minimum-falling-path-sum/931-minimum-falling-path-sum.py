class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        
        rows = len(matrix)
        cols = len(matrix[0])
        memo = defaultdict(int)
        # memoization
        def minPath(r,c):
            
            if not 0<=r<rows or not 0<=c<cols:
                return sys.maxsize
            
            if r == rows-1:
                return matrix[r][c]
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = min(minPath(r+1,c-1),minPath(r+1,c),minPath(r+1,c+1)) + matrix[r][c]
            return memo[(r,c)]
        
        result = sys.maxsize
        for i in range(cols):
            result = min(result,minPath(0,i))
            
        return result
                
            
        