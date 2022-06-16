class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        # Since the intervals are sorted binary search can be used to insert
        # O(N)
        bisect.insort_left(intervals,newInterval,0,len(intervals))
        print(intervals)
        flat = [intervals[0]]
        
        for i in range(1,len(intervals)):
            prevStart = flat[-1][0]
            prevEnd = flat[-1][1]
            
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            
            if currEnd > prevEnd and prevStart <= currStart <= prevEnd:
                flat[-1][1] = currEnd
                continue
                
            elif currStart >= prevStart and currEnd <= prevEnd:
                continue
                
            flat.append([currStart,currEnd])
            
        return flat
                
                
                
            
                
        