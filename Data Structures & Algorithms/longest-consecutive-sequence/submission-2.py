class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        set_nums = set(nums)
        for n in nums:
            if (n-1) not in set_nums:
                currLen = 1
                while (n+1) in set_nums:
                    currLen+=1
                    n+=1
                res = max(res,currLen)
        return res
