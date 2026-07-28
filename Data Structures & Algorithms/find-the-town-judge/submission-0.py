class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for source, destination in trust:
            delta[source]-=1
            delta[destination]+=1
        
        for person in range(1, n+1):
            if delta[person]==n-1:
                return person
        
        return -1