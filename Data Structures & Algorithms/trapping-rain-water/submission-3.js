class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        if(!height || height.length===0) return 0;
        let res=0
        let l=0,r=height.length-1
        let leftMax=height[l],rightMax=height[r]
        while(l<r){
            if(leftMax<rightMax){
                l++
                leftMax = Math.max(leftMax, height[l])
                res = res+ leftMax - height[l]
            } else{
                r--
                rightMax = Math.max(rightMax, height[r])
                res = res + rightMax - height[r]
            }
        }
        return res
    }
}
