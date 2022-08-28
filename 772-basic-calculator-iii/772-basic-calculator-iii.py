class Solution:
    def calculate(self, s: str) -> int:
        
        def update(op,num):
            if op == "+": stack.append(num)
            if op == "-": stack.append(-num)
            if op == "*": stack.append(stack.pop() * num)
            if op == "/": stack.append(int(stack.pop()/num))
                
                
        index,sign,stack,num = 0,"+",[],0
        
        while index < len(s):
            currChar = s[index]
            
            if currChar.isdigit():
                num = num*10 + int(currChar)
                
            elif currChar in "+-*/":
                update(sign,num)
                num,sign = 0,currChar
                
            elif currChar == "(":
                num,j = self.calculate(s[index+1:])
                index = index + j 
                
            elif currChar == ")":
                update(sign,num)
                return sum(stack), index + 1
            
            index += 1
            
        update(sign,num)
        return sum(stack)
            
        