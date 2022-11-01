class Solution:
    
    def findPermutation(self,nums):
        
        permutations = list(itertools.permutations(nums))
        return [int(''.join(permutation)) for permutation in permutations]
    
    def allSum(self,num):
        nums = [char for char in str(num)]
        result = sys.maxsize
        for i in range(len(nums)):
            if len(nums[:i])==0 or len(nums[:i])==0:
                continue
            for firstNum in self.findPermutation(nums[:i]):
                for secondNum in self.findPermutation(nums[i:]):
                    result = min(result,firstNum + secondNum)
            
            
        return result
    
    def minimumSum(self, num: int) -> int:
        result = sys.maxsize
        for x in self.findPermutation([char for char in str(num)]):
            result = min(result,self.allSum(x))
        return result
        
        
                
                
        
                
        
        
        
        
            
            
        