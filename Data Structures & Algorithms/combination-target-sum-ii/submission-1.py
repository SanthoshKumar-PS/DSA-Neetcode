class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, subset = [], []

        def dfs(start, cur):
            if cur==target:
                res.append(subset[:])
                return
            if cur>target:
                return
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                
                subset.append(candidates[i])
                dfs(i+1, cur+candidates[i])
                subset.pop()
            
        dfs(0,0)
        return res