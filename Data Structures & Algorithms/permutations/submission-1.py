class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res , subset = [], []
        perm = [False]*len(nums)

        def dfs():
            if len(subset)==len(nums):
                res.append(subset[:])
                return
            
            for i in range(len(nums)):
                if perm[i]:
                    continue
                subset.append(nums[i])
                perm[i] = True

                dfs()

                subset.pop()
                perm[i] = False
        dfs()
        return res