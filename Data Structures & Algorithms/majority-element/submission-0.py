class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        limit = (len(nums)//2)+1
        for n in nums:
            countMap[n] = 1+countMap[n]
            if countMap[n]>=limit:
                return n