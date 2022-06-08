class Solution(object):
    def containsDuplicate(self, nums):
        
        # Option 1 : Maintain previous state | Hashmap
        
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False
        