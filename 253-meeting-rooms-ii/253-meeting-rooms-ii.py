class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        order = defaultdict(int)
        
        for start,end in intervals:
            order[start] += 1
            order[end] -= 1
            
        rooms = 0
        maxRooms = 0
        for room in sorted(order):
            rooms += order[room]
            maxRooms = max(maxRooms,rooms)
            
        return maxRooms
            
        
        
        
        