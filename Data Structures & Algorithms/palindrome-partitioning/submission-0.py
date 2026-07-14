class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []

        def dfs(index):
            if index==len(s):
                res.append(path[:])
                return
            
            for i in range(index, len(s)):
                if self.isPalindrome(s, index, i):
                    path.append(s[index:i+1])
                    dfs(i+1)
                    path.pop()
        
        dfs(0)
        return res

    def isPalindrome(self, s, start, end):
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True