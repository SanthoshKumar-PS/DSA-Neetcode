class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let total = 1, prefix = new Array(nums.length).fill(1), suffix = new Array(nums.length).fill(1)
        for(let i=0;i<nums.length;i++){
            prefix[i]= total
            total = total*nums[i]
        }
        console.log("Prefix: ",prefix)
        total=1
        for(let i=nums.length-1;i>=0;i--){
            suffix[i] = total         
            total = total * nums[i]
        }
        console.log("Suffix: ",suffix)
        for(let i=0;i<nums.length;i++){
            nums[i]=prefix[i]*suffix[i]
        }
        return nums
    }
}
