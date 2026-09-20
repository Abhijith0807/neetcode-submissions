class Solution:
    def trap(self, height: List[int]) -> int:
        MinHeight  = [0]*len(height)
        currMax = 0
        for i in range(len(height)):
            MinHeight[i] = currMax
            currMax = max(currMax,height[i])
        currMax = 0
        for i in range(len(height)-1,-1,-1):
            MinHeight[i] = min(currMax,MinHeight[i])
            currMax = max(height[i],currMax)
        trappedWater = 0
        for i in range(len(height)):
            if MinHeight[i] - height[i]>0:
                trappedWater+=(MinHeight[i] - height[i])
        return(trappedWater)