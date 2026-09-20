class Solution:
    def helprob(self, nums: List[int]) ->int:
        rob1,rob2=0,0
        for i in nums:
            temp=max(rob2,i+rob1)
            rob1=rob2
            rob2=temp
        return(rob2)
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return(nums[0])
        return(max(self.helprob(nums[0:len(nums)-1]),self.helprob(nums[1:len(nums)])))
        