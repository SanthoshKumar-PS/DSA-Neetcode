class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        i = 0
        maxf = 0
        for j in range(len(s)):
            freq[s[j]] = 1 + freq.get(s[j],0)
            maxf = max(maxf, freq[s[j]])

            while (j-i+1)-maxf > k:
                freq[s[i]]-=1
                i+=1
            res = max(res, j-i+1)
        return res
    