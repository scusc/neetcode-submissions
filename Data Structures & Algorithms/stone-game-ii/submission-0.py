class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(isAliceTurn, index, M):
            if index == len(piles):
                return 0
            
            if (isAliceTurn, index, M) in dp:
                return dp[(isAliceTurn, index, M)]
            
            res = 0 if isAliceTurn else float('inf')
            total = 0

            for X in range(1, (2*M) + 1):
                if index + X > len(piles):
                    break
                
                total += piles[(index + X) - 1]
                if isAliceTurn:
                    res = max(res, total + dfs(not isAliceTurn, index + X, max(M, X)))
                else:
                    res = min(res, dfs(not isAliceTurn, index + X, max(M, X)))
            
            dp[(isAliceTurn, index, M)] = res
            return res
        
        return dfs(True, 0, 1)
        