class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<4 or len(s)>12:
            return []
        
        res, subset = [], []

        def dfs(index):
            if index==len(s):
                if len(subset)==4:
                    res.append(".".join(subset))
                return
            
            for j in range(index, min(index+3, len(s))):
                segment = s[index:j+1]

                if int(segment)>255:
                    continue
                if len(segment)>1 and segment[0]=='0':
                    continue
                
                subset.append(segment)
                dfs(j+1)
                subset.pop()
        dfs(0)
        return res
