class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,k = len(nums)-1,len(nums)-1

        while i>=0:
            if nums[i] == val:
                nums[k],nums[i] = nums[i], nums[k]
                k-=1
            i-=1
        return k+1