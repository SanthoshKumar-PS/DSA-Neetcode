class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, subset = [], []

        def dfs(open, close):
            if n*2==(open+close):
                res.append("".join(subset))
                return
            
            if open<n:
                subset.append('(')
                dfs(open+1, close)
                subset.pop()
            if open>close:
                subset.append(')')
                dfs(open, close+1)
                subset.pop()
        
        dfs(0,0)
        return res