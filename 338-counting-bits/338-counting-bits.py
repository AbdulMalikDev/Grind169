class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = [0]
        
        for i in range(1,n+1):
            currSum = sum([1 if x=='1' else 0 for x in str(bin(i))])
            result.append(currSum)
            
        return result
            
        