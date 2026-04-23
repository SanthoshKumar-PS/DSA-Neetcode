class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for let in s:
            dic[let] = 1 + dic.get(let,0)
        for i,let in enumerate(s):
            if let in dic and dic[let]==1:
                return i
        return -1