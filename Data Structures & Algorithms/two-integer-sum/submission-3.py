class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            required = target-nums[i]
            if required in freq:
                return [freq[required],i]
            freq[nums[i]] = i
        return [-1,-1]