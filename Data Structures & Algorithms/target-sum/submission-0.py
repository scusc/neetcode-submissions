from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = {0 : 1}

        for num in nums:
            newWays = defaultdict(int)
            for s in ways:
                newWays[s + num] += ways[s]
                newWays[s - num] += ways[s]
            ways = newWays
        return ways.get(target, 0)