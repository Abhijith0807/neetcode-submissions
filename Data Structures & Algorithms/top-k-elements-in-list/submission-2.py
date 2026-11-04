class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        countList = []
        for i,j in count.items():
            countList.append((-j,i))
        heapq.heapify(countList)
        res = []
        while k:
            res.append(heapq.heappop(countList)[1])
            k-=1
        return res