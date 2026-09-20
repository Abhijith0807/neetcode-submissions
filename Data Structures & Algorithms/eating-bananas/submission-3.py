class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lptr,rptr=1,max(piles)
        res=rptr
        while lptr<=rptr:
            k=(lptr+rptr)//2
            thrs=0
            for i in piles:
                thrs=thrs+math.ceil(float(i)/k)
            if thrs>h:
                lptr=k+1
            else:
                rptr=k-1
                res=k
        return(res)



        