class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        i=0
        tempSum = 0
        for i in range(len(nums)):
            tempSum+=nums[i]
            maxi = max(maxi, tempSum)
            if tempSum<0:
                tempSum = 0
        return maxi

