class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        fuelLeft = 0
        bestCityIndex = 0

        for i in range(len(gas)):
            fuelLeft += gas[i] - cost[i]

            if fuelLeft < 0:
                bestCityIndex = i + 1
                fuelLeft = 0
        return bestCityIndex