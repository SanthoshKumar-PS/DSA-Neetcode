class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const m = new Map();
        for(let str of strs){
            const key = str.split("").sort().join("")
            if(!m.has(key)){
                m.set(key,[])
            }
            m.get(key).push(str)
        }
        return Array.from(m.values())
    }
}
