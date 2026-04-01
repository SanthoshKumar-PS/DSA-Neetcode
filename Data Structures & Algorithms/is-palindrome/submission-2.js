class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        function isAlpha(char){
            return char.toLowerCase() !== char.toUpperCase();
        }
        function isNumeric(char){
            if(char===' ') return false
            return !isNaN(char)
        }

        let i=0,j=s.length-1
        while(i<j){
            while(i<j && !(isAlpha(s[i])||isNumeric(s[i]))){
                i++
            } 
            while(i<j && !(isAlpha(s[j]||isNumeric(s[j])))){
                j--
            }
            if(s[i].toLowerCase()!==s[j].toLowerCase()) return false

            i++
            j--
        }
        return true


    }
}
