class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {0}
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        for i in range(len(nums)):
            nextDp = set()
            for num in dp:
                if num+nums[i]==target:
                    return True
                nextDp.add(num+nums[i])
            dp.update(nextDp)
        return True if target in dp else False