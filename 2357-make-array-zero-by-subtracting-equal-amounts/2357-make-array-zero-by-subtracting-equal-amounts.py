class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        freq = set()
        for num in nums:
            if num!=0:
                freq.add(num)
                
        return len(freq)
        
        