class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows==1:
            return [[1]]
        res = self.generate(numRows-1)
        lastRow = res[-1]
        newRow = [1]
        for i in range(len(lastRow)-1):
            newRow.append(lastRow[i]+lastRow[i+1])
        newRow.append(1)

        res.append(newRow)
        return res