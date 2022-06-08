class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        # O(NlogN) Time | O(1) Space
        
        n = len(ransomNote)
        first = 0
        second = 0
        ransomNote = sorted(ransomNote) #O(NlogN) sorting
        magazine = sorted(magazine)
        
        for char in magazine:
            if char == ransomNote[first]:
                first += 1
                if first == n:
                    return True
                
                
        return False
                
        
        
        