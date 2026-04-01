class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const match = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        const stack = []
        for(let char of s){
            if(match[char]){
                const present = stack.pop();
                if(present!==match[char]) return false
            } else{
                stack.push(char)
            }
        }
        return stack.length!==0 ? false : true 
    }

}
