class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = []
        const list = ['+','-','*','/']
        let result = 0
        for(let token of tokens){
            if(!list.includes(token)){
                stack.push(Number(token))
            } else{
                const num2 = stack.pop()
                const num1 = stack.pop()
                if(token === '+'){
                    result = num1+num2
                }
                if(token === '-'){
                    result = num1-num2
                }
                if(token === '*'){
                    result = num1*num2
                }
                if(token === '/'){
                    result = Math.trunc(num1/num2)
                }
                stack.push(result)
            }
        }
        return stack.at(-1)
    }
}
