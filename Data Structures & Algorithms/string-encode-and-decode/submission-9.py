class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for st in strs:
            string+=f"{len(st)}#{st}"
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        i=0
        while i<len(s):
            num = ""
            string=""
            while s[i]!='#':
                num+=s[i]
                i+=1
            i+=1
            for val in range(int(num)):
                string+=s[i]
                i+=1
            strs.append(string)

        return strs
