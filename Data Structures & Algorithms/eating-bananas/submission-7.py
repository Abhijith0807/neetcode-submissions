class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = max(piles)
        while l<=r:
            k = (l+r)//2
            thres = 0
            for n in piles:
                thres+=math.ceil(float(n)/k)
            if thres>h:
                l = k+1
            else:
                r = k-1
                res= k 
        return(res)