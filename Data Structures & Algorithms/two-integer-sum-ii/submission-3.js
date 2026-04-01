class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        const map = new Map()
        for(let i=0;i<numbers.length;i++){
            let req = target - numbers[i]
            if(map.has(req)){
                return [map.get(req)+1,i+1]
            }
            map.set(numbers[i],i)            
        }
    }
}
