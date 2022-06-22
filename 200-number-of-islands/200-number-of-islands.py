class Solution:
    def bfs(self,node,grid):
        
        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node not in self.visited:
                self.visited.add(node)
                x,y = node
                for dx,dy in self.directions:
                    xx = x + dx
                    yy = y + dy
                    if 0<=xx<self.rows and 0<=yy<self.cols and grid[xx][yy]=="1":
                        queue.append((xx,yy))
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        result = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = ((1,0),(-1,0),(0,1),(0,-1),)
        self.visited = set()
        
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == "1" and (r,c) not in self.visited:
                    self.bfs((r,c),grid)
                    result += 1
        
        return result
        
        
        
        