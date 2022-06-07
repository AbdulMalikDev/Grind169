class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        
        # Idea is to perform a BFS on the matrix/image
        
        # Initializing variables
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        queue = deque([(sr,sc)])
        visited = set()
        rows = len(image)
        cols = len(image[0])
        startingColor = image[sr][sc]
        
        # Standard BFS Logic
        while queue:
            x,y = queue.popleft()
            if (x,y) not in visited:
                visited.add((x,y))
                image[x][y] = newColor
                for dx,dy in directions:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < rows and 0 <= yy < cols and image[xx][yy]==startingColor:
                        queue.append((xx,yy))
                        
                        
        return image
        