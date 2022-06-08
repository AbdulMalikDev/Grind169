class Solution(object):
    def longestCommonPrefix(self, strs):
        
        # If any empty string is found we know the result
        if any(len(x)==0 for x in strs):
            return ""
        
        seen = [0] * 200 # 200 since range given in problem description
        maxLen = max(len(x) for x in strs)
        prevChar = ""
        limit = 0
        
        # O(N * M) Time where N is length of longest string and M is no.of Strings
        for i in range(maxLen):
            for j in range(len(strs)):
                
                if i < len(strs[j]) and seen[i] == 0:
                    prevChar = strs[j][i]
                    
                if i<len(strs[j]) and strs[j][i] == prevChar:
                    seen[i] += 1
                    
            # i+1 because string splicing in python is exclusive not inclusive
            limit = i + 1
            
            if seen[i] != len(strs):
                # yes 'i' because we don't want to include this character
                limit = i
                break
                
        return strs[0][:limit]
            
            
            