class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let result = 0
        let l=0, r=heights.length-1
        while(l<r){
            const totalStore = Math.min(heights[l],heights[r]) * (r-l)
            result = Math.max(result,totalStore)
            if(heights[l]>heights[r]){
                r--
            } else{
                l++
            }
        }
        return result
    }
}
