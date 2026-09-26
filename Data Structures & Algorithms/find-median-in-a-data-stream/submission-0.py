class MedianFinder:

    def __init__(self):
        self.MaxHeap = []
        self.MinHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.MaxHeap,(-1)*num)
        if (self.MaxHeap and self.MinHeap and self.MaxHeap[0]*(-1)>self.MinHeap[0]):
            val = heapq.heappop(self.MaxHeap)*(-1)
            heapq.heappush(self.MinHeap,val)
        if len(self.MaxHeap)>len(self.MinHeap)+1:
            val = heapq.heappop(self.MaxHeap)
            heapq.heappush(self.MinHeap,(-1)*val)
        if len(self.MinHeap)>len(self.MaxHeap)+1:
            val = heapq.heappop(self.MinHeap)
            heapq.heappush(self.MaxHeap,(-1)*val)

    def findMedian(self) -> float:
        if len(self.MaxHeap)>len(self.MinHeap):
            return ((-1)*self.MaxHeap[0])
        elif len(self.MinHeap)>len(self.MaxHeap):
            return (self.MinHeap[0])
        else:
            return(((-1)*self.MaxHeap[0]+self.MinHeap[0])/2)
        