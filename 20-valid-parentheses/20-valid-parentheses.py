class Solution(object):
    
    def isOpeningBracket(self,char):
        if char == "(" or char == "{" or char == "[":
            return True
        return False
    
    def isSameType(self,bracket,char):
        if bracket == "(":
            return char == ")"
        elif bracket == "[":
            return char == "]"
        elif bracket == "{":
            return char == "}"
    
    def isValid(self, s):
        
        # This problem screams Stack so loud
        # since you want to keep track of previous state
        # in LIFO(last in first out) fasion
        
        stack = []
        
        for char in s:
            
            if self.isOpeningBracket(char):
                stack.append(char)
                
            else:
                if len(stack)==0:
                    return False
                # not same type of bracket
                if not self.isSameType(stack[-1],char):
                    return False
                stack.pop()
                
                
        return len(stack) == 0
                
        
        