class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        if(t==='') return ''
        const tCount = new Map();
        const window = new Map();
        for(let i=0; i<t.length;i++){
            tCount.set(t[i], (tCount.get(t[i])||0) +1)
        }
        
        let have= 0, need = tCount.size
        let l=0
        let result = [-1,-1] , resultLen=Infinity
        for(let r=0;r<s.length;r++){
            const c = s[r]
            window.set(c, (window.get(c)||0) +1)
            if(tCount.has(c) && window.get(c)===tCount.get(c)){
                have+=1
            }
            while(have===need){
                if((r-l+1) < resultLen){
                    resultLen = r-l+1
                    result = [l,r]
                }
                window.set(s[l],window.get(s[l])-1)
                if(tCount.has(s[l]) && window.get(s[l])<tCount.get(s[l])){
                    have-=1
                }
                l++
            }
        }

        return resultLen!==Infinity ? s.slice(result[0],result[1]+1) : '' 
    }
}
