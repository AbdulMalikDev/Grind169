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
                # Edge case if there are only closing brackets
                if len(stack)==0:
                    return False
                
                # not same type of bracket
                if not self.isSameType(stack[-1],char):
                    return False
                
                # If same type of bracket (Ideal case)
                stack.pop()
                
                
        return len(stack) == 0
    
    
    # Note how i've divided the code to be 'Modular' and divided it into functions 
    # instead of throwing everything into one function.
    # Also note function names and variables naming.
    # Commenting to understand logic flow
    # Also note how i've avoided using 'else' everywhere i'm using an 'if'
    # you can only do that if you really understand the program logic flow
                
        
        