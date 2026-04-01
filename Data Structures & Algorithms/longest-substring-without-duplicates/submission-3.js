class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        if(!s || s.length===0) return 0
        let l=0,r=0
        let maxP = 0
        const sett = new Set()
        while(r<s.length){
            while(sett.has(s[r])){
                sett.delete(s[l])
                l++
            }
            sett.add(s[r])
            maxP = Math.max(maxP, r-l+1)
            r++
        }
        return maxP
    }
}
