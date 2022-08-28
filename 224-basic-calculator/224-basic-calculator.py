class Solution:
    def calculate(self, s: str) -> int:
        
        def update(op,num):
            if op == "+": stack.append(num)
            if op == "-": stack.append(-num)
            if op == "*": stack.append(stack.pop() * num)
            if op == "/": stack.append(int(stack.pop() / num))
                
                
        it,sign,stack,num = 0,"+",[],0
        
        while it < len(s):
            
            if s[it].isdigit():
                num = num*10 + int(s[it])
                
            elif s[it] in "+-*/":
                update(sign,num)
                num,sign = 0,s[it]
                
            elif s[it] == "(":
                num,j = self.calculate(s[it+1:])
                it += j
                
            elif s[it] == ")":
                update(sign,num)
                return sum(stack),it + 1
            
            it += 1
            
        update(sign,num)
        return sum(stack)
        