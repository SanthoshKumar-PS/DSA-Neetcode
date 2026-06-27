class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []

        for point in points:
            x, y = point
            distance = x*x + y*y
            heapq.heappush(maxHeap, (-distance, point))
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        
        while maxHeap:
            _, point = heapq.heappop(maxHeap)
            res.append(point)
        
        return res