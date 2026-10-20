class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = { 0: 1 }
        res = 0
        prefixSum = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            req = prefixSum - k
            res += dic.get(req, 0)
            dic[prefixSum] = 1+dic.get(prefixSum, 0)
        return res