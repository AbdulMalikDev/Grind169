class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        result = [0] * (len(arr))
        previousLess = [-1] * len(arr)
        
        stack = []
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                previousLess[i] = stack[-1]
                
            stack.append(i)
            
        for i in range(len(arr)):
            result[i] = (result[previousLess[i]] or 0) + (i - previousLess[i]) * arr[i]
            
        return sum(result)  % (10**9+7)
                    
                
        
        
        