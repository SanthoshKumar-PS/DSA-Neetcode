class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {0: nums[0]}
        m = len(nums)
        def solve(n):
            if n<0:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = max(solve(n-1), nums[n]+solve(n-2))
            return memo[n]
        return solve(m-1)