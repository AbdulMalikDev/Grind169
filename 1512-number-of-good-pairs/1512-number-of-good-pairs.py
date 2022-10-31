class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        pos = defaultdict(list)
        result = 0
        
        for i in range(len(nums)):
            num = nums[i]
            pos[num].append(i)
            
            
        for number,indices in pos.items():
            n = len(indices)
            if n > 1:
                n = n-1
                result += (n*(n+1))//2
                
                
        return result
                
            
        