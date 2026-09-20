class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max,local_max=nums[0],nums[0]
        for r in range(1,len(nums)):
            local_max=max(nums[r],local_max+nums[r])
            if local_max>global_max:
                global_max=local_max
        return(global_max)