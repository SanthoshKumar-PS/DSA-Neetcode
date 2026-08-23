class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        state = [0]*numCourses
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            state[node] = 2
            result.append(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        result.reverse()
        return result