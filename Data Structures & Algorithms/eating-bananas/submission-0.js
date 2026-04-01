class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let l = 1, r = Math.max(...piles)
        let result = r
        while(l<=r){
            const k = Math.floor((l+r)/2) 
            let hours = 0
            for(let pile of piles){
                hours+= Math.ceil(pile/k)
            }
            if(hours<=h){
                result = Math.min(result, k)
                r=k-1
            } else{
                l=k+1
            }
        }
        return result
    }
}
