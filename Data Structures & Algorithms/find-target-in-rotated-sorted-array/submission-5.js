class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let res = -1
        let l=0, r=nums.length-1
        while(l<=r){
            const m = Math.floor((l+r)/2)
            console.log(nums[m])
            if(target === nums[m]) return m

            if(nums[l]<=nums[m]){
                if(nums[l]>target || nums[m]<target){
                    l=m+1
                } else{
                    r = m-1
                }
            } else{
                if(target<nums[m] || target>nums[r]){
                    r = m-1
                } else{
                    l=m+1
                }
            }
        }
        return -1
    }
}
