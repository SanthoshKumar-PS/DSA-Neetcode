class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = 0
        graph = defaultdict(list)
        queue = deque()
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        connected+=(n-len(graph))
        for key, valueList in graph.items():
            if key in visited:
                continue
            connected+=1
            queue.append(key)
            visited.add(key)
            
            while queue:
                popKey = queue.popleft()
                for node in graph[popKey]:
                    if node in visited:
                        continue
                    queue.append(node)
                    visited.add(node)
        return connected