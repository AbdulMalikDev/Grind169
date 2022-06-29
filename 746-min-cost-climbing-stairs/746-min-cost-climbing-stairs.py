class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = defaultdict(int)
        
        def steps(index):
            
            if index >= len(cost):
                return 0
            if index in memo:
                return memo[index]
            
            memo[index] = min(steps(index+1),steps(index+2)) + cost[index] 
            return memo[index]
        
        
        return min(steps(0),steps(1))
        
        
        