class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(x):
            res = curSum = l = 0
            for r in range(len(nums)):
                curSum+=nums[r]
                while curSum>x and l<=r:
                    curSum-=nums[l]
                    l+=1
                res+=(r-l+1)
            return res
        return atMost(goal) - atMost(goal-1)