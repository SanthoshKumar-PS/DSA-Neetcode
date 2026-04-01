class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums) {
        const map = new Map()
        for(let num of nums){
            let value = 0
            if(map.has(num)){
                value = map.get(num)
            }
            value+=1
            map.set(num,value)
        }
        let result=[]
        for(const [key,value] of map){
            if(value>(nums.length/3)){
                result.push(key)
            }
        }
        return result
    }
}
