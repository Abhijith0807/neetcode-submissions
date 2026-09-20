class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=list()
        curr=list()
        nums.sort()
        def buildset(i):
            if i==len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            buildset(i+1)
            curr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            buildset(i+1)
        buildset(0)
        return(res)