class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = []
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            first = i+1
            second = n-1
            while first < second:
                currSum = nums[first] + nums[second]
                if currSum > target:
                    second -= 1
                elif currSum < target:
                    first += 1
                else:
                    triplets.append([nums[i],nums[first],nums[second]])
                    first += 1
                    second -= 1
        
        duplicate = []
        for triplet in triplets:
            if triplet not in duplicate:
                duplicate.append(triplet)
                
        return duplicate
        