class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        rows = len(triangle)
        cols = [x for x in range(1,len(triangle)+1)]
        
        @lru_cache(None)
        def minPath(r,c):
            
            if not 0<=r<rows or not 0<=c<cols[r]:
                return sys.maxsize
            
            if r == rows-1:
                return triangle[r][c]
            
            option1 = minPath(r+1,c)
            option2 = minPath(r+1,c+1)
            
            return min(option1,option2)+triangle[r][c]
        
        return minPath(0,0)
        