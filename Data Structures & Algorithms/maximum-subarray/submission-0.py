class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        currSum=0
        for n in nums:
            currSum=currSum+n
            res=max(res,n,currSum)
            if currSum<0:
                currSum=0
        return(res)
        