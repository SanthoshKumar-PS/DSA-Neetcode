class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        def dfs(remaining):
            if remaining<0:
                return float('inf')
            if remaining in memo:
                return memo[remaining]
            
            minimum = float('inf')
            for coin in coins:
                result = dfs(remaining-coin)
                if result!=float('inf'):
                    minimum = min(minimum, result+1)
            memo[remaining] = minimum
            return minimum
        result = dfs(amount)
        return result if result!=float('inf') else -1