class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1]
        
        # store products from left in result array
        for i in range(len(nums)):
            num = nums[i]
            if i > 0:
                result.append(result[-1] * nums[i-1])
                
        print(result)
        right = 1
        # for right just maintain a varaible from the right side
        for i in reversed(range(len(nums))):
            # if i == 0:
            #     result[i] = right
            #     continue
            result[i] = result[i] * right
            right = right * nums[i]
        print(result)
        return result
                
                
        
        
            
            
        