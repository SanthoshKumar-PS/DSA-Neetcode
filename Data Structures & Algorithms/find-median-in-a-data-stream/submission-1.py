class MedianFinder:

    def __init__(self):
        self.small = [] #maxHeap
        self.large = [] #minHeap

    def addNum(self, num: int) -> None:
        if not self.small or num<=-self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)            
        
        if len(self.small)>len(self.large)+1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.small)+1<len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)


    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        elif len(self.small)<len(self.large):
            return self.large[0]
        return (-self.small[0]+self.large[0])/2.0
        
        
        