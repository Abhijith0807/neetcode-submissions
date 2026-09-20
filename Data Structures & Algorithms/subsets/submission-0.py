class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def buildset(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            buildset(i+1)
            subset.pop()
            buildset(i+1)
        buildset(0)
        return(res)
