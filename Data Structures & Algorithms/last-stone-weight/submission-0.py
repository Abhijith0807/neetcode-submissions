class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            firststone=heapq.heappop(stones)
            secondstone=heapq.heappop(stones)
            if firststone<secondstone:
                diff=firststone-secondstone
                heapq.heappush(stones,diff)
            
        if len(stones)>0:
            return(stones[0]*(-1))
        else:
            return(0)