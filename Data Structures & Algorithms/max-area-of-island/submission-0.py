class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        queue = deque()
        visited = set()
        directions = [ [1,0], [0,1], [-1,0], [0,-1] ]
        maximum_area = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 or (r,c) in visited:
                    continue
                queue.append([r,c])
                visited.add((r,c))
                area = 1
                while queue:
                    current_row, current_col = queue.popleft()
                    for dr, dc in directions:
                        neighbor_row, neighbor_col = current_row+dr, current_col+dc
                        if neighbor_row<0 or neighbor_row>=rows or neighbor_col<0 or neighbor_col>=cols or grid[neighbor_row][neighbor_col]==0 or (neighbor_row,neighbor_col) in visited:
                            continue
                        queue.append([neighbor_row,neighbor_col])
                        visited.add((neighbor_row,neighbor_col))
                        area+=1
                maximum_area = max(maximum_area, area)
        return maximum_area
                