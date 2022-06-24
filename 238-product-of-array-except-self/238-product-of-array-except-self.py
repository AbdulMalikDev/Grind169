class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Numbers:     2     3    4     5
        # Lefts:       1     2   2*3  2*3*4
        # Rights:    3*4*5  4*5   5     1
        
        result = [1]
        
        # store products from left in result array
        for i in range(len(nums)):
            num = nums[i]
            if i > 0:
                result.append(result[-1] * nums[i-1])
                
        right = 1
        # for right just maintain a varaible from the right side
        for i in reversed(range(len(nums))):
            result[i] = result[i] * right
            right = right * nums[i]
            
            
        return result
                
                
        
        
            
            
        