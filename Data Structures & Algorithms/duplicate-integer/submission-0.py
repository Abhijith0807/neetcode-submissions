class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictmap=dict()
        for i in nums:
            if i not in dictmap:
                dictmap[i]='True'
            else:
                return(True)
        return(False)
         