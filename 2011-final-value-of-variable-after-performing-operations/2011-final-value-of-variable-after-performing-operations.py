class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        x = 0
        ops = {"++X":1,"X++":1,"--X":-1,"X--":-1}
        
        for op in operations:
            
            x += ops[op]
            
        return x
        
        