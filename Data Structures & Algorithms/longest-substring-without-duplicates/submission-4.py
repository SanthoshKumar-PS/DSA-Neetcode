class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        res = 0
        dic = {}

        while i<=j and j<len(s):
            while s[j] in dic:
                del dic[s[i]]
                i+=1
            dic[s[j]] = j
            res = max(res, j-i+1)
            j+=1
        return res