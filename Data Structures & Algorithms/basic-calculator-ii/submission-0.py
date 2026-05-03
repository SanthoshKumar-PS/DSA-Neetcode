class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(' ','')
        print("s:",s)
        n = len(s)
        stack = []
        oper = '+'
        num = 0

        for i,let in enumerate(s):
            if let.isdigit():
                num = (num*10)+int(let)
            if (not let.isdigit()) or i==n-1:
                if oper=='+':
                    stack.append(num)
                elif oper=='-':
                    stack.append(-1*num)
                elif oper=='*':
                    stack.append(stack.pop()*num)
                elif oper=='/':
                    prev  =stack.pop()
                    stack.append(int(prev/num))
                oper = let
                num = 0
        return sum(stack)