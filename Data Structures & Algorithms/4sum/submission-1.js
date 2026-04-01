class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[][]}
     */
    fourSum(nums, target) {
        nums.sort((a,b)=>a-b)
        let result = []
        
        for(let i=0;i<nums.length;i++){
            if(i>0 && nums[i]===nums[i-1]) continue
            for(let j=i+1;j<nums.length;j++){
                if(j>i+1 && nums[j]===nums[j-1]) continue
                let start=j+1, end=nums.length-1
                while(start<end){
                    let sum = nums[i]+nums[j]+nums[start]+nums[end]
                    if(sum>target){
                        end--
                    } else if(sum<target){
                        start++
                    } else{
                        result.push([nums[i],nums[j],nums[start],nums[end]])
                        start++
                        while(start<end && nums[start]===nums[start-1]){
                            start++
                        }
                    }
                }
            }
        }
        return result
    }
}
