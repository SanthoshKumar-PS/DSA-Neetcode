class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = { 0:1 }
        res = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            req = prefix - k
            res += dic.get(req,0)
            dic[prefix] = 1 + dic.get(prefix,0)
        return res        