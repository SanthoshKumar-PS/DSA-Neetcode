class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        const map = new Map()
        for(let [i,num] of numbers.entries()){
            const required = target-num
            if(map.has(required)){
                return [map.get(required), i+1]
            }
            map.set(num,i+1)
        }
    }
}
