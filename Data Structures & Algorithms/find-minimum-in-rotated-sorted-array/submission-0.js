class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let l=0, r = nums.length-1
        let result = Infinity
        while(l<=r){
            const mid = Math.floor((l+r)/2)
            result = Math.min(result, nums[mid])
            if(nums[mid]>nums[r]){
                l = mid+1
            } else{
                r= mid-1
            }
        }
        return result

    }
}
