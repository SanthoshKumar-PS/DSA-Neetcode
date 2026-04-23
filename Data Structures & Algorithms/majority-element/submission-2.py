class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for num in nums:
            dic[num] = 1 + dic.get(num,0)
            if dic[num]>(n/2):
                return num
        return -1