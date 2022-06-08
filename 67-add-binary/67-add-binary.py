class Solution(object):
    def addBinary(self, a, b):
        
        # Neetcode video is good on this
        
        a = a[::-1]
        b = b[::-1]
        carry = 0
        result = ""
        
        for i in range(max(len(a),len(b))):
            
            digit1 = int(a[i]) if i < len(a) else 0
            digit2 = int(b[i]) if i < len(b) else 0
            
            total = digit1 + digit2 + carry
            
            # Same mod of 2
            char = str(total % 2)
            
            result = char + result
            
            # in case of '3', carry will be 1
            # in case of '2', carry will be 1
            # in case of '1', carry will be 0
            carry = total // 2
        
        if carry:
            result = "1" + result
        return result
        