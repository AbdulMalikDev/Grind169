class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n = len(days)
        dayNums = [1,7,30]
        memo = defaultdict(int)
        def minCost(reach,index):
            
            if (reach,index) in memo:
                return memo[(reach,index)]
            
            if reach > days[-1] or index==n:
                return 0
            
            if reach > days[index]:
                return minCost(reach,index+1)
            
            currDay = days[index]
            result = sys.maxsize
            for i in range(len(costs)):
                result  = min( result , minCost(currDay + dayNums[i],index+1) + costs[i] )
            
            memo[(reach,index)] = result
            return result
        
        return minCost(0,0)
        