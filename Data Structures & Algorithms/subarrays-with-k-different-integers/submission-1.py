class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(x):
            dic = {}
            l=0
            res=0
            for r in range(len(nums)):
                index = nums[r]
                dic[index] = 1 + dic.get(index,0)
                while len(dic)>x:
                    dic[nums[l]]-=1
                    if dic[nums[l]]==0:
                        del dic[nums[l]]
                    l+=1
                res+=(r-l+1)
            return res
        return atMost(k)-atMost(k-1)