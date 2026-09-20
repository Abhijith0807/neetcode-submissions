class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hashdp=dict()
        hashdp[len(cost)]=0
        hashdp[len(cost)-1]=cost[len(cost)-1]
        curr=len(cost)-2
        while curr>=0:
            hashdp[curr]=min(cost[curr]+hashdp[curr+1],cost[curr]+hashdp[curr+2])
            curr=curr-1
        return(min(hashdp[0],hashdp[1]))
