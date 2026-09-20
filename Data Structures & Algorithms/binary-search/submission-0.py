class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lptr=0
        rptr=len(nums)-1
        while lptr<=rptr:
            mid=(lptr+rptr)//2
            if nums[mid]==target:
                return(mid)
            elif nums[mid]<target:
                lptr=mid+1
            else:
                rptr=mid-1
        return(-1)
        