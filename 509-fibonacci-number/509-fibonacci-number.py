class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
        
    def fib(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]
    
    # Time complexity : O(n) [Observe how function calls increase with n]
    # Space complexity also O(n) since no.of function calls == stack length
        