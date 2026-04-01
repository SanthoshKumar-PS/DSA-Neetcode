class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    rotate(nums, k) {
        let n = nums.length
        k = k%n
        nums.reverse()
        let start = 0, end = k-1
        while(start<end){
            let temp = nums[start]
            nums[start] = nums[end]
            nums[end]= temp
            start++
            end--
        }
        start = k,end = n-1
        while(start<end){
            let temp = nums[start]
            nums[start] = nums[end]
            nums[end]= temp
            start++
            end--
        }
    }
}
