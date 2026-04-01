class Solution {
    /**
     * @param {number[]} people
     * @param {number} limit
     * @return {number}
     */
    numRescueBoats(people, limit) {
        people.sort((a,b)=>a-b)
        let i=0,j=people.length-1
        let total=0
        while(i<=j){
            let remain = limit-people[j]
            j--
            total++
            if(i<=j && remain>=people[i]){
                i++
            }
        }
        return total

    }
}
