class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        frPro=dict()
        rvPro=dict()
        for i in range(len(nums)):
            if i==0:
                frPro[i]=1
            else:
                frPro[i]=frPro[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                rvPro[i]=1
            else:
                rvPro[i]=rvPro[i+1]*nums[i+1]

        res=list()
        for i in range(len(nums)):
            res.append(frPro[i]*rvPro[i])
        return(res)