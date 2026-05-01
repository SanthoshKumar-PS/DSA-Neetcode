class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''

        for let in s:
            if let!=']':
                stack.append(let)
            else:
                tempStr = []
                while stack and stack[-1]!='[':
                    tempStr.append(stack.pop())
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                finalStr = int(k)*"".join(reversed(tempStr))
                stack.append(finalStr)
        return "".join(stack)