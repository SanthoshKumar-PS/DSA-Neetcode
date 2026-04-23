class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} 
        for i,num in enumerate(nums):
            req = target-num
            if req in dic:
                return [dic[req],i]
            dic[num] = i
        return [-1,-1]
