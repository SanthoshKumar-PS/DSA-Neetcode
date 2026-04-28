class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for let in s:
            if let in close:
                if stack and stack[-1]==close[let]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(let)
        return True if not stack else False