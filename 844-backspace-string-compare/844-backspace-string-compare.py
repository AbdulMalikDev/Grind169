class Solution(object):
    def removeBackspace(self,string):
        
        backspace = 0
        newString = ""
        pointer = 0
        while pointer < len(string):
            
            if string[pointer] == "#":
                backspace += 1
                
            else:
                if backspace > 0:
                    backspace -= 1
                else:
                    newString = newString + string[pointer]
                
            pointer += 1
        return newString[::-1]
    
    def backspaceCompare(self, s, t):
        
        # trick / intuition : REVERSE the strings
        
        s = self.removeBackspace(s[::-1])
        t = self.removeBackspace(t[::-1])
        return s == t
        
                
            
        