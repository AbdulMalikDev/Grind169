class Solution(object):
    def twoSum(self, nums, target):
        
        
        # # O(n**2) Time O(1) Space
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
#         O(N) Time | O(N) Space 
#         missingNums = {}
#         for index,num in enumerate(nums):
#             missingNum = target - num 
#             if missingNum in missingNums:
#                 return [index,missingNums[missingNum]]
            
#             missingNums.update({num : index})

        # Two pointers method
        # O(NlogN)
        
        # Indices need to be stored since sorting rearranges
        indices = defaultdict(list)
        for i in range(len(nums)):
            indices[nums[i]].append(i)
        # print(indices)
        nums.sort() 
        first = 0
        last = len(nums)-1
        
        while first<last:
            currSum = nums[first] + nums[last]
            if currSum == target:
                # Exception case
                if nums[first] == nums[last]:
                    return [indices[nums[first]][0],indices[nums[last]][1]]
                
                return [indices[nums[first]][0],indices[nums[last]][0]]
            
            if currSum > target:
                last -= 1
            else:
                first += 1
                
        
        
        
        