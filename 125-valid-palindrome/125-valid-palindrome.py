class Solution(object):
    def sanitizeString(self,string):
        newString = []
        for char in string:
            isNumber = 48<=ord(char)<=57
            if char.isalpha() or isNumber:
                if ord(char) <= 90 and not isNumber:
                    char = chr(ord(char) + 32)
                newString.append(char)
        return "".join(newString)
    
    def isPalindromeHelper(self,string):
        first = 0
        last = len(string)-1
        
        while first < last:
            if string[first] != string[last]:
                return False
            first += 1
            last -= 1
            
        return True
    
    def isPalindrome(self, s):
        s = self.sanitizeString(s)
        return self.isPalindromeHelper(s)
        