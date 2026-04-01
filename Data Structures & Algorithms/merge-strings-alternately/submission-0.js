class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {string}
     */
    mergeAlternately(word1, word2) {
        if(!word1 && !word2) return ""
        if(!word1) return word2
        if(!word2) return word1

        let i=0
        let result = ""
        while(i<word1.length && i<word2.length){
            result=result + word1[i] + word2[i]
            i++
        }
        result+=word1.slice(i)
        result+=word2.slice(i)
        return result
    }
}
