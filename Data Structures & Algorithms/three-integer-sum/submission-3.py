class Solution:
    def twoSum(self, nums:List[int], target: int):
        lptr,rptr=0,len(nums)-1
        result=list()
        while lptr<rptr:
            diff=target-nums[lptr]
            if diff==nums[rptr]:
                result.append([nums[lptr],nums[rptr]])
                lptr+=1
            elif diff>nums[rptr]:
                lptr+=1
            else:
                rptr-=1
        return(result)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=list()
        nums=sorted(nums)
        for i in range(len(nums)):
            target=(-1)*nums[i]
            currList=self.twoSum(nums[i+1:],target)
            for j in currList:
                x=[nums[i]]
                x.extend(j)
                if x not in res:
                    res.append(x)
        return(res)
        