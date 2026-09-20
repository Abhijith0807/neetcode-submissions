class TimeMap:

    def __init__(self):
        self.Map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.Map[key]
        l,r = 0,len(arr)-1
        res = ''
        while l<=r:
            mid = (l+r)//2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid+1
            else:
                r = mid-1
        return(res)
