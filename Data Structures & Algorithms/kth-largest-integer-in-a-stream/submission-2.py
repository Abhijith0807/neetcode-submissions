class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.mynums=nums
        heapq.heapify(self.mynums)
        while len(self.mynums)>self.k:
            heapq.heappop(self.mynums)
    def add(self, val: int) -> int:
        heapq.heappush(self.mynums,val)
        while len(self.mynums)>self.k:
            heapq.heappop(self.mynums)
        return(self.mynums[0])
        
