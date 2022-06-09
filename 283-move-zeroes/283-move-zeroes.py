class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        nonZeroes = []
        
        for num in nums:
            if num!=0:
                nonZeroes.append(num)
        n = len(nonZeroes)-1
        for i in range(len(nums)):
            
            if i > n:
                nums[i] = 0
                continue
                
            nums[i] = nonZeroes[i]
                
            
            
            
            
            
        
        
        