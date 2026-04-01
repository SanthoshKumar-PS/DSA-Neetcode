class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        res = 0
        dic = {}

        while i<=j and j<len(s):
            if s[j] in dic:
                i = max(dic[s[j]]+1,i)
            dic[s[j]] = j
            res = max(res, j-i+1)
            j+=1
        return res