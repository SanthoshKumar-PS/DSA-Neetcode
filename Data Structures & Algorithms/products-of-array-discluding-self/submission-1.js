class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let prefix = Array(nums.length).fill(1);
        let suffix = Array(nums.length).fill(1);
        let prod=1
        for(let i=0;i<nums.length;i++){
            prefix[i] = prod
            prod = prod*nums[i]
        }
        console.log(prefix)
        prod=1
        for(let i=nums.length-1;i>=0;i--){
            suffix[i]=prod
            prod = prod*nums[i]
        }
        console.log(suffix)
        for(let i=0;i<nums.length;i++){
            prefix[i] = prefix[i]*suffix[i]
        }
        return prefix
    }
}
