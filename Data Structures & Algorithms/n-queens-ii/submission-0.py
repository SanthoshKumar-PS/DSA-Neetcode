class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        cols = set()
        diag = set()
        antidiag = set()

        def dfs(row):
            if row==n:
                self.res+=1
                return
            
            for col in range(n):
                if col in cols or row-col in diag or row+col in antidiag:
                    continue
                
                cols.add(col)
                diag.add(row-col)
                antidiag.add(row+col)

                dfs(row+1)

                cols.remove(col)
                diag.remove(row-col)
                antidiag.remove(row+col)
        dfs(0)
        return self.res