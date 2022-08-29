class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        zero = s.count("0")
        one = 0
        result = zero
        
        for char in s:
            zero -= char=="0"
            one += char=="1"
            result = min(result,zero+one)
            
        return result
        