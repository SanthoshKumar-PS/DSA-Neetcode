class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for let in magazine:
            dic[let] = 1 + dic.get(let,0)
        for let in ransomNote:
            if let in dic and dic[let]>0:
                dic[let]-=1
            else:
                return False
        return True