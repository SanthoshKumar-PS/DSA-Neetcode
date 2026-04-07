class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        l=0
        for r in range(len(nums)):
            if nums[r] in dic:
                if abs(r - dic[nums[r]])<=k:
                    return True
            dic[nums[r]] = r
        return False 