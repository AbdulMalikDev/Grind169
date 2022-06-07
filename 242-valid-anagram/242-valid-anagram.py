class Solution(object):
    def isAnagram(self, s, t):
        
        # O(NlogN) Time | O(1) Space
        return sorted(s) == sorted(t)
    
        # O(N) Time | O(N) Space
        chars = defaultdict(str)
        for char in s:
            chars[char] = char
        
        for char in t:
            if char not in chars:
                return False
            
            
        return True
    
        # Note : This 2nd technique can also be used in sliding window 
        # in some problems