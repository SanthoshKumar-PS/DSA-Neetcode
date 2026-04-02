class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tMap = {}
        for let in t:
            tMap[let] = 1 + tMap.get(let,0)
        have, need = 0, len(tMap)
        sMap = {}
        i = 0
        res = [-1,-1]
        minLen = float('infinity');
        for j in range(len(s)):
            if s[j] in tMap:
                sMap[s[j]] = 1 + sMap.get(s[j],0)
                if sMap[s[j]]==tMap[s[j]]:
                    have+=1
            
            while have == need:
                if minLen>j-i+1:
                    minLen = j-i+1
                    res = [i,j]
                if s[i] in sMap:
                    sMap[s[i]]-=1
                if s[i] in sMap and sMap[s[i]]<tMap[s[i]]:
                    have-=1
                i+=1
        l,r = res    
        return s[l:r+1] if minLen!=float('infinity') else ""
