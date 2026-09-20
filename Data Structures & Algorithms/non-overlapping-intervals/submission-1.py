class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        heapq.heapify(intervals)
        testInterval=heapq.heappop(intervals)
        while len(intervals)!=0:
            currInterval=heapq.heappop(intervals)
            if currInterval[0]>=testInterval[1]:
                testInterval[1]=currInterval[1]
            else:
                count+=1
                testInterval[1]=min(testInterval[1],currInterval[1])
        return(count)