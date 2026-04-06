class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        curSum = 0
        for i in range(k):
            curSum += arr[i]
        res = curSum
        l = 0
        for r in range(k, len(arr)):
            curSum+=arr[r]
            curSum-=arr[l]
            res = max(res,curSum)
            l+=1
        return res
