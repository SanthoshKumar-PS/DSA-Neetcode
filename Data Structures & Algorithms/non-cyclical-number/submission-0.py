class Solution:
    def isHappy(self, n: int) -> bool:
        sett  = set()
        while n not in sett:
            sett.add(n)
            n = self.sumOfSquares(n)

            if n==1:
                return True

        return False
    def sumOfSquares(self, n: int) -> int:
        total = 0
        while n:
            lastNum = n%10
            total+=lastNum**2
            n=n//10
        return total