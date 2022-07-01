class Solution:
    def binarySearch(self,nums,target):
        
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        
        def condition(left,mid) -> bool:
            return nums[0] > nums[mid]

        
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if condition(left,mid):
                right = mid
            else:
                left = mid + 1
        # print(left)
        result1 = self.binarySearch(nums[:left],target)
        result2 = self.binarySearch(nums[left:],target)
        result2 = left + result2 if result2 != -1 else result2
        return max(result1,result2)
        