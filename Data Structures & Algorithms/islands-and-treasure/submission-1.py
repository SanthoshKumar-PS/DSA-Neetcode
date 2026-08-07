class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        visited = set()
        queue = deque()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==-1 or grid[i][j]==2147483647:
                    continue
                queue.append(((i, j), 0))
                visited.add((i,j))
        while queue:
            (r, c), distance = queue.popleft()
            for dr, dc in directions:
                cr, cc = dr+r, dc+c
                if cr<0 or cr==ROWS or cc<0 or cc==COLS or grid[cr][cc]==-1 or (cr,cc) in visited:
                    continue
                grid[cr][cc]=distance+1
                queue.append(((cr,cc),distance+1))
                visited.add((cr,cc))
        