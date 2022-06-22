class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        rotten = []
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        visited = set()
        fresh = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh.add((r,c))
                    
        queue = deque(rotten)
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                if (x,y) not in visited:
                    visited.add((x,y))
                    for dx,dy in directions:
                        xx = x + dx
                        yy = y + dy
                        if 0<=xx<rows and 0<=yy<cols and grid[xx][yy]==1:
                            grid[xx][yy]=2
                            fresh.remove((xx,yy))
                            queue.append((xx,yy))
            if queue:
                minutes += 1
                
        return minutes if len(fresh)==0 else -1
                
        
        
        
        
        