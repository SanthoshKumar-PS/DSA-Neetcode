class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            dic[fruits[r]]+=1
            while len(dic)>2:
                index = fruits[l]
                dic[index] -= 1
                if dic[index]==0:
                    del dic[index]
                l+=1
            res = max(res,r-l+1)
        return res
        