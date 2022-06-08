class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if any(len(x)==0 for x in strs):
            return ""
        
        seen = [0] * 200
        maxLen = max(len(x) for x in strs)
        prevChar = ""
        limit = 0
        for i in range(maxLen):
            
            for j in range(len(strs)):
                
                if i < len(strs[j]) and seen[i] == 0:
                    prevChar = strs[j][i]
                    
                if i<len(strs[j]) and strs[j][i] == prevChar:
                    seen[i] += 1
                    
            limit = i + 1
            if seen[i] != len(strs):
                limit = i
                break
                
        return strs[0][:limit]
            
            
            