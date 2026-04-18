class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        
        def dfs(left, right):
            if left > right:
                return 0
            
            if (left, right) in dp:
                return dp[(left, right)]
            
            isEvenLen = (right - left) % 2 == 0
            leftPile = piles[left] if isEvenLen else 0
            rightPile = piles[right] if isEvenLen else 0

            dp[(left, right)] = max(dfs(left + 1, right) + leftPile, dfs(left, right - 1) + rightPile)
            return dp[(left, right)]
        
        total = sum(piles)
        aliceScore = dfs(0, len(piles) - 1)
        return aliceScore > total - aliceScore
        