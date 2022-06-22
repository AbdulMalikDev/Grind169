class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # We will maintain a Max Heap of k elements
        # for every element after heap length greater than k
        # we will check if distance is less than max, if yes pop and add
        # else ignore. Its a technique to get top k smallest/largest
        # using Heap
        
        heap = []
        
        for x,y in points:
            
            dist = x**2+y**2
            if len(heap) < k:
                heapq.heappush(heap,(-dist,(x,y)))
            else:
                if dist < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dist,(x,y)))
            
        return [list(y) for x,y in heap ]