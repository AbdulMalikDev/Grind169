class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        
        
        # Tabulation
        dp = [0 for _ in range(days[-1]+1)]
        days = set(days)
        
        for i in range(len(dp)):
            
            if i in days:
                dp[i] = min(dp[max(0,i-1)]+cost[0],dp[max(0,i-7)]+cost[1],dp[max(0,i-30)]+cost[2]) 
            else:
                dp[i] = dp[i-1]
            
        return dp[-1]
            
        
        # recursion & memoization
#         n = len(days)
#         dayNums = [1,7,30]
#         memo = defaultdict(int)
#         def minCost(reach,index):
            
#             if (reach,index) in memo:
#                 return memo[(reach,index)]
            
#             if reach > days[-1] or index==n:
#                 return 0
            
#             if reach > days[index]:
#                 return minCost(reach,index+1)
            
#             currDay = days[index]
#             result = sys.maxsize
#             for i in range(len(costs)):
#                 result  = min( result , minCost(currDay + dayNums[i],index+1) + costs[i] )
            
#             memo[(reach,index)] = result
#             return result
        
#         return minCost(0,0)
        