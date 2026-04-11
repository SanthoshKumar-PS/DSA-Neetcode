class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(x):
            count = res = l = 0
            for r in range(len(nums)):
                count+=nums[r]
                while count>x and l<=r:
                    count-=nums[l]
                    l+=1
                res+=(r-l+1)
            return res

        return atMost(goal)-atMost(goal-1)