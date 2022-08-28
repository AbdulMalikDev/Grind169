class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        memo = defaultdict()
        
        def areWordsContained(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i:j] in words:
                memo[(i,j)] = True
                return True
            
            result = False
            for k in range(i+1,j):
                result = result or (areWordsContained(i,k) and areWordsContained(k,j))
                
            memo[(i,j)] = result
            return result
        
        
        return areWordsContained(0,len(s))
        