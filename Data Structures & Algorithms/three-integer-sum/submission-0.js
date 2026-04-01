class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        if(!nums) return []
        nums = nums.sort((a,b)=>a-b)
        let result = []
        for(let i=0;i<nums.length-2;i++){ 
            if(i>0 && nums[i]===nums[i-1]) continue
            let start=i+1,end=nums.length-1
            while(start<end){
                let sum = nums[i]+nums[start]+nums[end]
                if(sum>0){
                    end--
                } else if(sum<0){
                    start++
                } else{
                    result.push([nums[i],nums[start],nums[end]])
                    start++
                    while(start<end && nums[start]===nums[start-1]){
                        start++
                    }
                }
            }
        }
        return result
    }
}
