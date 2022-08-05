class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = defaultdict(int)
        def combinations(sum):
            
            if sum in memo:
                return memo[sum]
            
            if sum == 0:
                return 1
            
            result = 0
            for index in range(n):
                # choose number
                if nums[index] <= sum:
                    result += combinations(sum-nums[index])
                
            memo[sum] = result
            return memo[sum]
        
        return combinations(target)