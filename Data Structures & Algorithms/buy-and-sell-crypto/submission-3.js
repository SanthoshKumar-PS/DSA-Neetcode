class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        if(!prices || prices.length==0) return 0

        let l=0,r=1
        let maxP = 0
        while(r<prices.length){
            if(prices[l]<prices[r]){
                const profit = prices[r]-prices[l]
                maxP = Math.max(maxP, profit)
            }
            else{
                l=r
            }
            r++

        }
        return maxP
    }
}
