class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = ''
        for(let str of strs){
            result+=str.length+'#'+str
        }
        console.log(result)
        return result
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i=0,len = str.length
        let result=[]
        while(i<len){
            console.log("i: ",i)
            let j=i
            let num = ''
            while(j<len && str[j]!=='#'){
                num+=str[j]
                j++
            }
            j++
            let newStr=''
            for(let k=j;k<j+Number(num);k++){
                newStr+=str[k]
            }
            result.push(newStr)
            i=j+Number(num)
            console.log(newStr)
        }
        return result    }
}
