class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        resMax=-1
        while left<right:
            res=(right-left)*(min(heights[left],heights[right]))
            resMax=max(resMax,res)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return(resMax)


        