class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isAlphanumeric(char){
        return (
            (char>='a' && char<='z') ||
            (char>='A' && char<='Z') ||
            (char>='0' && char<='9')
        )

    }
    isPalindrome(s) {
        if(!s) return true
        let i=0,j=s.length-1
        while (i<j){
            while(i<j & !this.isAlphanumeric(s[i])){
                i++
            }
            while(i<j & !this.isAlphanumeric(s[j])){
                j--
            }
            if(s[i].toLowerCase()!==s[j].toLowerCase()){
                return false
            }
            i++
            j--
        }
        return true
        
    }
}
