class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set(nums)
        print(len(nums),len(uniq))
        if(len(nums) == len(uniq)):
            return False
        else:
            return True
        