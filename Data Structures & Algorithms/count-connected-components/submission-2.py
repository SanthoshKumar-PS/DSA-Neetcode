class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = 0
        graph = defaultdict(list)
        queue = deque()
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            if node in visited:
                continue
            connected+=1
            queue.append(node)
            visited.add(node)
            
            while queue:
                popnode = queue.popleft()
                for neigh in graph[popnode]:
                    if neigh in visited:
                        continue
                    queue.append(neigh)
                    visited.add(neigh)
        return connected