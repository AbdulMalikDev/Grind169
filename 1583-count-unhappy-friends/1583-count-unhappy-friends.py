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
        print(preferences)
        print(pairs)
        
        for key,value in preferences.items():
            
            for char in value:
                if pairs[key] == char:
                    break
                indexOfKey = preferences[char].index(key)#1
                indexOfPair = preferences[char].index(pairs[char])#2
                print(indexOfKey)
                print(indexOfPair)
                if indexOfPair > indexOfKey:
                    print(char)
                    print(key)
                    result += 1
                    break
                print("")
        return result