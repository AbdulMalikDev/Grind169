class Solution:
    def unhappyFriends(self, n: int, pref: List[List[int]], prs: List[List[int]]) -> int:
        
        
        result = 0
        
        preferences = defaultdict(list)
        pairs = defaultdict(int)
        
        for index,value in enumerate(pref):
            preferences[index] = value
            
        for a,b in prs:
            pairs[a] = b
            pairs[b] = a
        
        for key,value in preferences.items():
            
            for char in value:
                if pairs[key] == char:
                    break
                    
                indexOfKey = preferences[char].index(key)
                indexOfPair = preferences[char].index(pairs[char])
                
                if indexOfPair > indexOfKey:
                    result += 1
                    break
                    
        return result