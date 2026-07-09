class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []
        perm = [False]*len(nums)

        def dfs():
            if len(nums)==len(subset):
                res.append(subset[:])
                return
            
            for i in range(len(nums)):
                if perm[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not perm[i-1]:
                    continue
                
                subset.append(nums[i])
                perm[i] = True

                dfs()

                subset.pop()
                perm[i] = False
        dfs()
        return res