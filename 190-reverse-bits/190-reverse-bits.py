class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0
        
        for _ in range(32):
            
            # left shift result
            result = result << 1
            
            # Add the last digit of n to result
            result += n % 2
            
            # right shift n to get rid of last digit recently added
            n = n >> 1
            
            
        return result
        
        
        
        