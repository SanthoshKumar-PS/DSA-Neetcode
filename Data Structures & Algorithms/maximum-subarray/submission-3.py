class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        i=0
        tempSum = 0
        while(i<len(nums)):
            tempSum+=nums[i]
            maxi = max(maxi, tempSum)
            if tempSum<0:
                tempSum = 0
            i+=1
        return maxi

