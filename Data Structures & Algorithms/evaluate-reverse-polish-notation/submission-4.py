class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sett = { '+', '-', '*', '/' }
        for let in tokens:
            if let not in sett:
                stack.append(int(let))
            else:
                b = stack.pop()
                a = stack.pop()
                if let=='+':
                    stack.append(a+b)
                elif let=='-':
                    stack.append(a-b)
                elif let=='*':
                    stack.append(a*b)
                elif let=='/':
                    stack.append(int(float(a)/b))
        return stack[0]