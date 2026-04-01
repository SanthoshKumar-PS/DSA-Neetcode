class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        let len = nums.length;
        const map = new Map();
        for (const num of nums) {
            map.set(num, (map.get(num) || 0) + 1)
            if(map.get(num)>len/2) return num
        }
    }
}
