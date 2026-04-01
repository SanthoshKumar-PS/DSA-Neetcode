class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const stack = []
        const result = new Array(temperatures.length).fill(0)
        for(let r=temperatures.length-1;r>=0;r--){
            while(stack && temperatures[stack[stack.length-1]]<=temperatures[r]){
                stack.pop()
            }
            let distance = (stack[stack.length-1] - r) || 0
            result[r]=(distance)
            stack.push(r)
        }
        return result
    }
}
