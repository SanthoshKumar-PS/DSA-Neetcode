class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        visited = set()
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0 or (row, col) in visited:
                    continue
                
                queue.append((row, col))
                visited.add((row,col))
                area = 0
                while queue:
                    r, c = queue.popleft()
                    area+=1
                    for dr, dc in directions:
                        cr, cc = r+dr, c+dc
                        if cr<0 or cr==len(grid) or cc<0 or cc==len(grid[0]) or (cr,cc) in visited or grid[cr][cc]==0:
                            continue
                        queue.append((cr,cc))
                        visited.add((cr,cc))
                maxArea = max(maxArea, area)
        return maxArea