class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        # Tabulation
        
        dp = [0 for _ in range(len(cost)+1)]
        
        dp[1] = cost[0]
        dp[2] = cost[1]
        
        for i in range(3,len(cost)+1):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i-1]
        
        
        return min(dp[-1],dp[-2])
        
        
#         memoized Version
        
#         memo = defaultdict(int)
        
#         def steps(index):
            
#             if index >= len(cost):
#                 return 0
#             if index in memo:
#                 return memo[index]
            
#             memo[index] = min(steps(index+1),steps(index+2)) + cost[index] 
#             return memo[index]
        
        
#         return min(steps(0),steps(1))
        
        
        