class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = { 0: -1 }
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            req = total%k
            if req not in remainder:
                remainder[req] = i
            elif i - remainder[req]>1:
                return True
        return False