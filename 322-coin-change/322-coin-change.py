class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = defaultdict(int)
        def change(changeSum):
            
            if changeSum in memo:
                return memo[changeSum]
            
            if changeSum == 0:
                return 0
            # elif changeSum < 0:
            #     return sys.maxsize
            
            result = sys.maxsize
            for coin in coins:
                if coin <= changeSum:
                    result = min(result,1+change(changeSum-coin))
                    
            # ⭐️ Memoization. Remembering the optimized amount 
            # and no.of coins needed for it.
            memo[changeSum] = result
            return result
        
        result = change(amount)
        return -1 if result==sys.maxsize else result
        