class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid), len(grid[0])
        queue = deque()
        islands = 0
        visited = set()
        directions = [ [0,1], [1,0], [-1,0], [0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="0" or (r,c) in visited:
                    continue
                islands+=1
                queue.append([r,c])
                visited.add((r,c))
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in directions:
                        row, col = cr+dr, cc+dc
                        if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]!="1":
                            continue
                        if (row, col) in visited:
                            continue
                        queue.append([row,col])
                        visited.add((row,col))
        return islands
