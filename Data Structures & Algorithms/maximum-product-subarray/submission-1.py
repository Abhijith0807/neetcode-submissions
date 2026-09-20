class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        maxp,minp=1,1
        for n in nums:
            tmp=maxp*n
            maxp=max(n,n*maxp,n*minp)
            minp=min(n,tmp,n*minp)
            res=max(res,maxp)
        return(res)