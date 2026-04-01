class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const m = matrix.length
        const n = matrix[0].length
        let low = 0, high = m*n-1
        while(low<=high){
            const mid = Math.floor((low+high)/2)
            const row = Math.floor(mid/n)
            const col = mid%n
            if(matrix[row][col] < target){
                low = mid+1
            } else if(matrix[row][col] > target){
                high = mid-1
            } else{
                return true
            }
        }
        return false
    }
}
