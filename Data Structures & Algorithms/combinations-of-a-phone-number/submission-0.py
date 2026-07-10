class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res, subset = [], []
        keyboard = {
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(index):
            if index==len(digits):
                res.append("".join(subset))
                return
            word = keyboard[digits[index]]
            for letter in word:
                subset.append(letter)
                dfs(index+1)

                subset.pop()


        dfs(0)
        return res