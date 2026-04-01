class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const occur = {}
        for (let i=0;i<nums.length;i++){
            let req = target - nums[i]
            console.log(req)
            if(req in occur){
                console.log("Yes found")
                return [occur[req],i]
            }
            occur[nums[i]] = i
        }
        return [-1,-1]
    }
}
