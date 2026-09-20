class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPos=len(nums)-1
        currPos=len(nums)-2
        while goalPos!=0:
            if currPos<0:
                return(False)
            else:
                if currPos+nums[currPos]>=goalPos:
                    goalPos=currPos
                    currPos-=1
                else:
                    currPos-=1
        return(True)
        