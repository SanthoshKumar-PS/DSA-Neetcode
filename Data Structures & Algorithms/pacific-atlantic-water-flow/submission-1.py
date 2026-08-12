class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(heights), len(heights[0])
        for j in range(COLS):
            pacific.add((0, j))
            atlantic.add((ROWS - 1, j))
        for i in range(ROWS):
            pacific.add((i, 0))
            atlantic.add((i, COLS - 1))

        def BFS(queue, visited):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        nr < 0
                        or nr == ROWS
                        or nc < 0
                        or nc == COLS
                        or (nr, nc) in visited
                        or heights[r][c] > heights[nr][nc]
                    ):
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        pacific_queue = deque(pacific)
        BFS(pacific_queue, pacific)
        atlantic_queue = deque(atlantic)
        BFS(atlantic_queue, atlantic)

        return list(atlantic & pacific)
