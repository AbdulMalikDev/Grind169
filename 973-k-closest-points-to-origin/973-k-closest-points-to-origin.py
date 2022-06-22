class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result = []
        heap = []
        for x,y in points:
            heapq.heappush(heap,(x**2+y**2,(x,y)))
            
        for _ in range(k):
            distance,coords = heapq.heappop(heap)
            result.append(list(coords))
            
        return result