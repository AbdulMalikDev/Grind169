class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        result = []
        negative = -1
        positive = len(nums)
        
        for index,num in enumerate(nums):
            if num < 0:
                negative = index
                
            else:
                positive = index
                break
                
        while negative >= 0 and positive < len(nums):
            
            if nums[negative]**2 <= nums[positive]**2:
                result.append(nums[negative]**2)
                negative -= 1
            else:
                result.append(nums[positive]**2)
                positive += 1
                
        while negative >= 0:
            result.append(nums[negative]**2)
            negative -= 1
        while positive < len(nums):
            result.append(nums[positive]**2)
            positive += 1
            
            
        return result            
                
        
        