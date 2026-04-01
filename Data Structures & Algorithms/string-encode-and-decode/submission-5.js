class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = ""
        for(let i=0;i<strs.length;i++){
            let str = strs[i]
            result+=str.length.toString()+'#'+str
        }
        return result
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i=0
        let result=[]
        while (i<str.length){
            let num=""
            while(i<str.length && str[i]!=='#'){
                num+=str[i]
                i++
            }
            i++
            const length = Number(num)
            result.push(str.slice(i,i+length))
            i+=length

        }
            return result

    }
    }
