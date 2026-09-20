class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while nums[l]>nums[r]:
            mid=(l+r)//2
            if mid==l or mid==r:
                break
            elif nums[mid]>nums[l]:
                l=mid
            elif nums[mid]<nums[r]:
                r=mid
        return(min(nums[l],nums[r]))