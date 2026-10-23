class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffixMax = [0]*len(arr)
        currMax = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            suffixMax[i] = currMax
            currMax = max(currMax,arr[i])
        suffixMax[-1] = -1
        return suffixMax