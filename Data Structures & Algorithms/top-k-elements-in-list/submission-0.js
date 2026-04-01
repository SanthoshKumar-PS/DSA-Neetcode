class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let freq = {}
        for (let num of nums) {
            if (freq[num]) {
                freq[num] = freq[num] + 1
            }
            else {
                freq[num] = 1
            }
        }
        console.log(freq)
        const sorted = Object.entries(freq).sort((a, b) => b[1] - a[1]);

        let result = []
        for(let i=0;i<k;i++){
            result.push(sorted[i][0])
        }
        return result
    }
}
