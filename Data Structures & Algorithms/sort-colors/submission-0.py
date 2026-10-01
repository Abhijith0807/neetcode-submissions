class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z,curr,t = 0,0,len(nums)-1
        while curr <= t:
            if nums[curr] == 0:
                nums[curr],nums[z] = nums[z],nums[curr]
                z+=1
                curr+=1
            elif nums[curr] == 1:
                curr+=1
            elif nums[curr] == 2:
                nums[curr],nums[t] = nums[t],nums[curr]
                t-=1
            