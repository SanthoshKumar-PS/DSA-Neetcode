class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks or len(tasks)==0:
            return 0
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0

        while maxHeap or queue:
            time+=1
            if maxHeap:
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time+n])
            
            if queue and time==queue[0][1]:
                cnt, curTime = queue.popleft()
                heapq.heappush(maxHeap, cnt)
        return time