class MinStack {
    constructor() {
        this.stack = []
        this.minStack = []
    }


    push(val) {
        this.stack.push(val)
        let minVal = Math.min(val, this.minStack.length===0?val: this.minStack[this.minStack.length-1])
        this.minStack.push(minVal)
    }

    /**
     * @return {void}
     */
    pop() {
        this.stack.pop()
        this.minStack.pop()
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length-1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minStack[this.minStack.length-1]
    }
}
