class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const hashSet = new Set(nums)
        let maxi = 0, result = 0
        for(let num of nums){
            if(!hashSet.has(num-1)){
                while(hashSet.has(num+maxi)){
                    maxi++
                }
                result = Math.max(result,maxi)
            }
            maxi=0
        }
        return result
    }
}
