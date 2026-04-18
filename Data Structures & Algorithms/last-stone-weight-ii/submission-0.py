class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        n = len(stones)

        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for tar in range(1, target + 1):
                if stones[i - 1] <= tar:
                    dp[i][tar] = max(dp[i - 1][tar], dp[i - 1][tar - stones[i - 1]] + stones[i - 1])
                else:
                    dp[i][tar] = dp[i - 1][tar]
        return stoneSum - 2 * dp[n][target]
        