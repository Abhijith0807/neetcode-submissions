class TimeMap:

    def __init__(self):
        self.MapRecord=dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.MapRecord:
            self.MapRecord[key]=dict()
            self.MapRecord[key][timestamp]=value
        else:
            self.MapRecord[key][timestamp]=value            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.MapRecord:
            return('')
        else:
            nums=list(self.MapRecord[key].keys())
            nums.sort()
            if timestamp in nums:
                return(self.MapRecord[key][timestamp])
            else:
                l,r=0,len(nums)-1
                res=''
                while l<=r:
                    m=(l+r)//2
                    if nums[m]<=timestamp:
                        res=self.MapRecord[key][nums[m]]
                        l=m+1
                    else:
                        r=m-1
                return(res)
            
