class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        dic = [0]*26
        for i in range(len(s)):
            dic[ord(s[i]) - ord('a')]+=1
            dic[ord(t[i]) - ord('a')]-=1
        for i in range(26):
            if dic[i]!=0:
                return False
        return True