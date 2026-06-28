class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        ans = []

        for num in arr:
            distance = abs(num-x)
            heapq.heappush(maxHeap,(-distance,-num))
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)

        while maxHeap:
            ng_distance, ng_num = heapq.heappop(maxHeap)
            ans.append(-ng_num)
        
        ans.sort()
        return ans