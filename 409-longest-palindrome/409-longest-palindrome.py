class Solution(object):
    def longestPalindrome(self, s):
        
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
            
        odd = False
        even = 0
        
        for char,frequency in freq.items():
            if frequency % 2 == 0:
                even += frequency
            else:
                odd = True
                even += (frequency-1)
                
                
        return even + odd
        