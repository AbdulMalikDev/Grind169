class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # In this condition make sure there are k-1 elements smaller than this value
        def condition(value,rows,cols):
            elements = 0
            col = cols-1
            for row in range(rows):
                while col >= 0 and matrix[row][col] > value:
                    col -= 1
                elements += (col+1)
            return elements
                        
                
        
        # kth smallest element means there are exactly k-1 elements on left
        rows = len(matrix)
        cols = len(matrix[0])
        left = matrix[0][0]
        right = matrix[-1][-1]+1
        
        while left < right:
            
            mid = (left+right)//2
            
            midResult = condition(mid,rows,cols) 
            print(mid)
            print(midResult)
            print(" ")
            if midResult >= k:
                right = mid
            else:
                left = mid + 1
                
        
        # left is the minimal x satisfying the condition
        print(right)
        return left