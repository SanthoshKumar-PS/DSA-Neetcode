class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        for num in nums:
            nextDp = {}
            for curSum, count in dp.items():
                add = curSum + num
                sub = curSum - num
                nextDp[add] = nextDp.get(add,0) + count
                nextDp[sub] = nextDp.get(sub,0) + count
            dp = nextDp
        return dp.get(target, 0)