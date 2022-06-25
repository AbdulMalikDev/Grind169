class Solution:
    
    def check(self,nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
    def checkPossibility(self, nums: List[int]) -> bool:
        return any(self.check(nums[:x]+nums[x+1:]) for x in range(len(nums)))
#         heap = []
#         error = 0
#         for num in nums:
#             heapq.heappush(heap,-num)
            
#             while heap and -heap[0] > num:
#                 error += 1
#                 if error > 1:
#                     return False
#                 heapq.heappop(heap)
                
#         return True
    
    
        
#         error = 0
#         for i in range(len(nums)-1):
#             currNum = nums[i]
#             nextNum = nums[i+1]
            
#             if currNum > nextNum:
#                 error += 1
#                 if error > 1:
#                     return False
                
#         return True
                
        
        