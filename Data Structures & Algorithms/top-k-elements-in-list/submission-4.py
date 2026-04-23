class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num,0)
        res = []
        sort = sorted(dic.items(),key=lambda x:x[1],reverse=True)
        for key,value in sort:
            if k>0:
                res.append(key)
                k-=1
        return res