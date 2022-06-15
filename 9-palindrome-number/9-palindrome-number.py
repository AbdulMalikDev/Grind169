class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x%10 == 0 and x!=0):
            return False
        
        reversedNumber = 0
        while reversedNumber < x:
            # print(reversedNumber)
            # print(x)
            # print("")
            # add last digit of x to reversed number
            reversedNumber = reversedNumber * 10 + (x % 10)
            # Getting rid of last digit of x
            x = x // 10
        
        return (x == reversedNumber or (x == (reversedNumber // 10))) 
        