class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        testInterval=heapq.heappop(intervals)
        res=list()
        while len(intervals)!=0:
            currInterval=heapq.heappop(intervals)
            if testInterval[1]<currInterval[0]:
                res.append(testInterval)
                testInterval=currInterval
            elif testInterval[0]>currInterval[1]:
                res.append(currInterval)
            else:
                testInterval[0]=min(testInterval[0],currInterval[0])
                testInterval[1]=max(testInterval[1],currInterval[1])
        res.append(testInterval)
        return(res)