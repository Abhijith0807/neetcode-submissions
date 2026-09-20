"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        allintervals=list()
        for inv in intervals:
            allintervals.append((inv.start,inv.end))
        if not allintervals:
            return(True)
        heapq.heapify(allintervals)
        endtime=heapq.heappop(allintervals)[1]
        while len(allintervals)>0:
            currtime=heapq.heappop(allintervals)
            if currtime[0]>=endtime:
                endtime=currtime[1]
            else:
                return(False)
        return(True)