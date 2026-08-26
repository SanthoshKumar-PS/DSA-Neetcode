class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for st in strs:
            count = [0]*26
            for let in st:
                count[ord(let)-ord('a')]+=1
            dic[tuple(count)].append(st) 
        return list(dic.values())