class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    rotate(nums, k) {
        const arr = new Array(nums.length)
        k=k%nums.length
        for(let i=0;i<nums.length;i++){
            arr[(i+k )% nums.length] = nums[i] 
        }
        for(let i=0;i<nums.length;i++){
            nums[i] = arr[i]
        }
        return nums
    }
}
