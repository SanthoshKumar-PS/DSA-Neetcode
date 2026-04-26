class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        for num in sett:
            if num-1 not in sett:
                curNum = num
                count = 0
                while curNum in sett:
                    curNum+=1
                    count+=1
                res = max(res, count)
        return res