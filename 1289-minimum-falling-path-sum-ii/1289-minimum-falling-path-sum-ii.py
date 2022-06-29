class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        memo = defaultdict(int)
        valueToRow = defaultdict(set)
        
        # memoization
        def minPath(r,c):
            
            if not 0<=r<rows or not 0<=c<cols:
                return sys.maxsize
            
            if r == rows-1:
                memo[(r,c)] = matrix[r][c]
                return memo[(r,c)]
            
            if (r,c) in memo:
                # print(r,c,matrix[r][c])
                return memo[(r,c)]
            
            # Make sure that there is no precalculated Value in same row
            if r in valueToRow[matrix[r][c]]:
                for j in range(cols):
                    if (r,j) in memo and matrix[r][j]==matrix[r][c]:
                        memo[(r,c)] = min(memo[(r,j)],minPath(r+1,j)+matrix[r][c])
                        break
            else:
                # Also serves as default value
                minCost = sys.maxsize
                for j in range(cols):
                    if j != c:
                        if (r+1,j) in memo:
                            minCost = min(minCost,memo[(r+1,j)])
                        else:
                            minCost = min(minCost,minPath(r+1,j))

                memo[(r,c)] = minCost + matrix[r][c]
                valueToRow[matrix[r][c]].add(r)
            
            return memo[(r,c)]
        
        result = sys.maxsize
        for i in range(cols):
            result = min(result,minPath(0,i))
            
        return result
        