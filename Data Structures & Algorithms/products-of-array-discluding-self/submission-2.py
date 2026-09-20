class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd=[1]*len(nums)
        postProd=[1]*len(nums)
        for i in range(len(nums)):
            if i!=0:
                preProd[i]=preProd[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i!=len(nums)-1:
                postProd[i]=postProd[i+1]*nums[i+1]
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=preProd[i]*postProd[i]
        return(res)
