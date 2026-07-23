class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==0:
            return []
        res = []
        board = [['.']*n for _ in range(n)]
        cols = set()
        diag = set()
        antidiag = set()

        def dfs(row):
            if row==n:
                res.append(["".join(crow) for crow in board])
                return
            for col in range(n):
                if col in cols or row-col in diag or row+col in antidiag:
                    continue
                
                cols.add(col)
                diag.add(row-col)
                antidiag.add(row+col)
                board[row][col] = 'Q'

                dfs(row+1)

                cols.remove(col)
                diag.remove(row-col)
                antidiag.remove(row+col)
                board[row][col] = '.'

        dfs(0)
        return res