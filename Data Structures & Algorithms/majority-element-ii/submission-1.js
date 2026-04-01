class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums) {
        let num1=null,num2=null,count1=0,count2=0
        for(let num of nums){
            if(num===num1){
                count1++
            } else if(num===num2){
                count2++
            } else if(count1===0){
                num1=num
                count1=1
            } else if(count2===0){
                num2=num
                count2=1
            } else{
                count1--
                count2--
            }
        }
        // num1=2,count1=2,num2=2,count2=3
        let t1=0,t2=0
        for(let num of nums){
            if(num===num1){
                t1++
            } else if(num===num2){
                t2++
            } else{
                continue
            }
        }
        let result=[]
        if(t1>Math.floor(nums.length/3)){
            result.push(num1)
        } 
        if(t2>Math.floor(nums.length/3)){
            result.push(num2)
        }
        return result
    }
}
