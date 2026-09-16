class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def solve(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==0 and j==0:
                memo[(i,j)] = grid[i][j]
                return grid[i][j]
            if i==0:
                ans = grid[i][j] + solve(i, j-1)
                memo[(i,j)] = ans
                return ans
            if j==0:
                ans = grid[i][j] + solve(i-1,j)
                memo[(i,j)] = ans
                return ans
            ans = grid[i][j] + min(solve(i,j-1), solve(i-1,j))
            memo[(i,j)] = ans
            return ans
        return solve(m-1, n-1)