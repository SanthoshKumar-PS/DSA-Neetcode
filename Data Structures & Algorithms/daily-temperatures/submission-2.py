class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                top = stack.pop()
                topIndex = top[1]
                res[topIndex] = i-topIndex 
            stack.append((temperatures[i],i))
        return res