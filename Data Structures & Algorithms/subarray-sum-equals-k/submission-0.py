class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = defaultdict(int)
        prefixMap[0] = 1
        res,currSum = 0,0
        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefixMap.get(diff,0)
            prefixMap[currSum] = 1 + prefixMap.get(currSum,0)
        return res