class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(len(nums)):
            summ=0
            for j in range(i, len(nums)):
                summ+=nums[j]
                result = max(result,summ)
        return result
