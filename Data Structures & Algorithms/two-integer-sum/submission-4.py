class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            req = target-nums[i]
            if req in freq:
                return [freq[req],i]
            freq[nums[i]] = i
        return [-1,-1]
        