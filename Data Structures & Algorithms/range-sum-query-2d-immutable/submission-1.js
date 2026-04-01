class NumMatrix {
    /**
     * @param {number[][]} matrix
     */
    constructor(matrix) {
        const rows = matrix.length;
        const cols = matrix[0].length;
        const prefix = Array.from({length:rows+1},()=>Array(cols+1).fill(0))
        for(let i=1;i<prefix.length;i++){
            for(let j=1;j<prefix[0].length;j++){
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1] 
            }
        }
        this.prefixMatrix = prefix
    }

    /**
     * @param {number} row1
     * @param {number} col1
     * @param {number} row2
     * @param {number} col2
     * @return {number}
     */
    sumRegion(row1, col1, row2, col2) {
        const regionSum = (
            this.prefixMatrix[row2+1][col2+1] 
            - this.prefixMatrix[row1][col2+1] 
            - this.prefixMatrix[row2+1][col1] 
            + this.prefixMatrix[row1][col1])
        return regionSum
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
