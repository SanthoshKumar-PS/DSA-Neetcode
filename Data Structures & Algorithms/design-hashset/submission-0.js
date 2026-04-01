class MyHashSet {
    constructor() {
        this.set = [];
    }

    /**
     * @param {number} key
     * @return {void}
     */
    add(key) {
        if(this.set.includes(key)){
            return null
        }
        this.set.push(key)
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        this.set = this.set.filter(num=>num!==key)
        
    }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        return this.set.includes(key)
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
