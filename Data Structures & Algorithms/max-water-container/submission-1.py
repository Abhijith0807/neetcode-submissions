class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr,rptr=0,len(heights)-1
        resAmt=0
        while lptr<rptr:
            currAmt=min(heights[lptr],heights[rptr])*(rptr-lptr)
            resAmt=max(resAmt,currAmt)
            if heights[lptr]<heights[rptr]:
                lptr+=1
            elif heights[lptr]>heights[rptr]:
                rptr-=1
            else:
                lptr+=1
                rptr-=1
        return(resAmt)