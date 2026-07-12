class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r, c , index):
            if len(word)==index:
                return True
            
            if r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c]!=word[index] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = dfs(r+1, c, index+1) or dfs(r-1, c, index+1) or dfs(r, c+1, index+1) or dfs(r, c-1, index+1)
            visited.remove((r,c))

            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False