class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*num for num in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            out = abs(-s1 - (-s2))
            if out>0:
                heapq.heappush(stones,-out)

        return -stones[0] if stones else 0