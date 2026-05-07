class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            req = prefix - k
            res += dic.get(req, 0)
            dic[prefix] = 1 + dic.get(prefix, 0)
        return res   