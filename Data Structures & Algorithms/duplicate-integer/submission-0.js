class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const sett = new Set();
        for (const num of nums){
            if(sett.has(num)){
                return true
            }
            sett.add(num);
        }
        return false
    }
}
