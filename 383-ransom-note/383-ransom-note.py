class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        
        # Bruteforce O(N*M) where N is ransomNote len and M magazine len
        # Check every letter in ransomNote with Magazine

        
        # O(NlogN) Time | O(1) Space
#         n = len(ransomNote)
#         first = 0
#         second = 0
#         ransomNote = sorted(ransomNote) #O(NlogN) sorting
#         magazine = sorted(magazine)
        
#         for char in magazine:
#             if char == ransomNote[first]:
#                 first += 1
#                 if first == n:
#                     return True
                
#         return False

        # O(N) Time | O(N) Space
    
        letters = defaultdict(int)
        
        for char in magazine:
            letters[char] += 1
            
        for char in ransomNote:
            if char not in letters or letters[char] <= 0:
                return False
            letters[char] -= 1
            
        return True
            
        

        
                
        
        
        