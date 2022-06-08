class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        n = len(ransomNote)
        first = 0
        second = 0
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        
        # O(N) Time | O(1) Space
        for char in magazine:
            if char == ransomNote[first]:
                first += 1
                if first == n:
                    return True
                
                
        return False
                
        
        
        