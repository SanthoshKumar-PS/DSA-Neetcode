class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        dic[0]=1
        curSum, res = 0,0
        for r in range(len(nums)):
            curSum+=nums[r]
            diff = curSum - goal
            if diff in dic:
                res+=dic[diff]
            dic[curSum]+=1
        return res