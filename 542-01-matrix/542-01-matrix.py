class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # Note : This works exactly like Topological sort
        # cells with distance 0 are first processed than
        # 1 etc.
        
        rows = len(mat)
        cols = len(mat[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        visited = set()
        allZeroes = []
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    allZeroes.append((r,c))
                else:
                    # Unprocessed
                    mat[r][c] = -1
                    
        queue = deque(allZeroes)
        
        while queue:
            x,y = queue.popleft()

            for dx,dy in directions:
                xx = x + dx
                yy = y + dy
                if 0<=xx<rows and 0<=yy<cols and mat[xx][yy] == -1:

                    mat[xx][yy] = mat[x][y] + 1
                    queue.append((xx,yy))
                
                
        return mat
        