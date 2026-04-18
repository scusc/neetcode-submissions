class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp = [-9999] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            total = 0

            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                dp[i] = max(dp[i], total - dp[j + 1])
        
        res = dp[0]
        if res == 0:
            return "Tie"
        return "Alice" if res > 0 else "Bob"