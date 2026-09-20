class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        res=[]
        for x in points:
            distance=math.sqrt(math.pow(x[0],2)+math.pow(x[1],2))
            heapq.heappush(h,(distance,x))
        while k>0:
            res.append(heapq.heappop(h)[1])
            k-=1
        return(res)
        