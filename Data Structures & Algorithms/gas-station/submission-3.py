class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return(-1)
        totalGas=0
        startpoint=0
        for i in range(len(gas)):
            totalGas+=(gas[i]-cost[i])
            if totalGas<0:
                totalGas=0
                startpoint=i+1
        return(startpoint)
