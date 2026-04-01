class Solution {

    getConcatenation(nums) {
        let ans=[]
        for(let j=0;j<2;j++){
        for(let i=0;i<nums.length;i++){
            ans.push(nums[i])
        }
        }
        return ans
    }
}
