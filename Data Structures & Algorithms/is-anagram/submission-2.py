class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        dic = [0]*26
        for i in range(len(s)):
            s_ind = ord(s[i]) - ord('a')
            t_ind = ord(t[i]) - ord('a')
            dic[s_ind]+=1
            dic[t_ind]-=1
        for i in range(26):
            if dic[i]!=0:
                return False
        return True