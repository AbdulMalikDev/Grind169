class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [0]*3
        col = [0]*3
        ld = 0
        rd = 0
        currPlayer = 1
        
        for a,b in moves:
            row[a] += currPlayer
            col[b] += currPlayer
            if a == b:
                ld += currPlayer
            if a + b == 2:
                rd += currPlayer
                
            if any(abs(x)==3 for x in row) or any(abs(x)==3 for x in col) or abs(rd)==3 or abs(ld)==3:
                return "A" if currPlayer==1 else "B"
            
            currPlayer *= -1
            
        print(row)
        print(col)
        print(ld)
        print(rd)
        return "Draw" if len(moves)==9 else "Pending"
        