class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result = []
        heap = []
        for x,y in points:
            dist = x**2+y**2
            if len(heap) < k:
                heapq.heappush(heap,(-dist,(x,y)))
            else:
                if dist < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dist,(x,y)))
                
            
#         for _ in range(k):
#             distance,coords = heapq.heappop(heap)
#             result.append(list(coords))
            
        return [list(y) for x,y in heap ]