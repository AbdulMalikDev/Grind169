class Solution:
    def largestVariance(self, s: str) -> int:
        
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        letters = set(s)
        if len(letters) == len(s) or len(letters)==1:
            return 0
        maxResult = 0
        print(freq)
        # Implement kadane for each letter
        for a in ascii_lowercase:
            for b in ascii_lowercase:
                if a!=b:
                    aCount = freq[a]
                    bCount = freq[b]
                    has_a,has_b = False,False
                    maxCount = 0
                    rollingCount = 0
                    
                    for char in s:
                        if char not in [a,b]:
                            continue
                        if rollingCount<0 and aCount>0 and bCount>0:
                            has_a,has_b = False,False
                            rollingCount = 0
                        if char == a:
                            rollingCount += 1
                            aCount -= 1
                            has_a = True
                        if char == b:
                            bCount -= 1
                            rollingCount -= 1
                            has_b = True
                        if has_a and has_b:
                            maxCount = max(rollingCount,maxCount)
                    maxResult = max(maxResult,maxCount)
            
            
        return maxResult 
        