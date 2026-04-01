class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if(s1.length>s2.length) return false
        const s1array = new Array(26).fill(0)
        const s2array = new Array(26).fill(0)

        for(let i=0;i<s1.length;i++){
            s1array[s1.charCodeAt(i)-97]++
            s2array[s2.charCodeAt(i)-97]++
        }

        const isSame = (arr1,arr2) => {
            for(let i=0;i<26;i++){
                if(arr1[i]!==arr2[i]) return false
            }
            return true
        }

        for(let i=0;i<s2.length-s1.length;i++){
            if(isSame(s1array,s2array)) return true
            s2array[s2.charCodeAt(i+s1.length)-97]++
            s2array[s2.charCodeAt(i)-97]--
        }

        return isSame(s1array,s2array)

    }
}
