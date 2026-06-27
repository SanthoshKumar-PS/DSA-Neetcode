class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minHeap = []
        res = []
        for num, count in freq.items():
            heapq.heappush(minHeap,(count,num))
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        
        while len(minHeap):
            count, num = heapq.heappop(minHeap)
            res.append(num)

        return res