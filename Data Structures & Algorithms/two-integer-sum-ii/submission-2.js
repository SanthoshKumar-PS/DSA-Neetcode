class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let i=0,j=1
        const map = new Map()
        while(i<numbers.length){
            let req = target - numbers[i]
            if(map.has(req)){
                return [map.get(req)+1,i+1]
            }
            map.set(numbers[i],i)
            i++

            
        }
    }
}
