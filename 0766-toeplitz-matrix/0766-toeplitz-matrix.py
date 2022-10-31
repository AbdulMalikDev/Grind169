class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        diagnols = defaultdict(int)
        
        for i in range(rows):
            for j in range(cols):
                
                diagnol = i - j
                if diagnol in diagnols and diagnols[diagnol] != matrix[i][j]:
                    return False
                
                diagnols[diagnol] = matrix[i][j]
                
        return True
        
        
            
        