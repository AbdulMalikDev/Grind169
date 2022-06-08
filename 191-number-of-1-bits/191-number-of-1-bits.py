class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return sum([1 if x=='1' else 0 for x in str(bin(n))])
        