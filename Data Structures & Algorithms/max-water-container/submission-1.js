class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left=0,right=heights.length-1
        let area=0
        while(left<right){
            let min_height = Math.min(heights[left], heights[right])
            let length = right-left
            area = Math.max(area,min_height*length)
            if(heights[left]>heights[right]){
                right--
            } else{
                left++
            }
        }
        return area
    }
}
