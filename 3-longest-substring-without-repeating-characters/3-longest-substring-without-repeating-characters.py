class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lastSeen = defaultdict(int)
        windowStart,windowLen = 0,0
        for windowEnd in range(0,len(s)):
            
            endChar = s[windowEnd]
            if endChar not in lastSeen:
                lastSeen[endChar] = windowEnd
            else:
                # Important point here ⬇️
                if windowStart < lastSeen[endChar] + 1: 
                    windowStart = lastSeen[endChar] + 1
                lastSeen[endChar] = windowEnd
                
            windowLen = max(windowLen, windowEnd - windowStart + 1)
            
        return windowLen
        