class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        queue = deque()

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        
        for course in range(numCourses):
            if indegree[course]==0:
                queue.append(course)
            
        finished = 0
        while queue:
            node = queue.popleft()
            finished+=1

            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        return numCourses==finished