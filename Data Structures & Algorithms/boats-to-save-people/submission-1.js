class Solution {
    /**
     * @param {number[]} people
     * @param {number} limit
     * @return {number}
     */
    numRescueBoats(people, limit) {
        let totalBoats=0
        people.sort((a,b)=>a-b)
        let i=0,j=people.length-1
        while(i<=j){
            let remain = limit-people[j]
            j--
            totalBoats++
            if(i<=j && remain>=people[i]){
                i++
            }
        }
        return totalBoats
    }
}
