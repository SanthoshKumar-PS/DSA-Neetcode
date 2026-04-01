class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        const cars = position.map((pos,i)=>[pos,speed[i]])
        cars.sort((a,b)=>b[0]-a[0])
        const stack = []
        for(let car of cars){
            const time = (target-car[0])/car[1]
            if(stack.length==0 || stack[stack.length-1]<time){
                stack.push(time)
            }            
            console.log(stack)

        }
        return stack.length

    }
}
