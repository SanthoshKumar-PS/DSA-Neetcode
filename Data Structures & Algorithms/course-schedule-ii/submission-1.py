class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        indegree = [0]*numCourses
        queue = deque()

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        
        for course in range(numCourses):
            if indegree[course]==0:
                queue.append(course)
            
        while queue:
            course = queue.popleft()
            res.append(course)
            
            for neigh in graph[course]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        return res if len(res)==numCourses else []