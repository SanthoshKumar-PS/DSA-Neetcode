class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        canditate = None
        count = 0 

        for num in nums:
            if count==0:
                canditate = num
                count+=1
            elif count>0 and canditate==num:
                count+=1
            else:
                count-=1
        return canditate