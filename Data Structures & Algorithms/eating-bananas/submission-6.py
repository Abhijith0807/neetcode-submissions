class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lptr,rptr=1,max(piles)
        res=rptr
        while lptr<=rptr:
            thrs=0
            k=(lptr+rptr)//2
            for n in piles:
                thrs=thrs+math.ceil(float(n)/k)
            if thrs>h:
                lptr=k+1
            else:
                rptr=k-1
                res=k
        return(res)