class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap=dict()
        res=list()
        for i in nums:
            if i not in hashMap:
                hashMap[i]=1
            else:
                hashMap[i]+=1
        bucket=[[] for i in range(len(nums)+1)]
        for key,val in hashMap.items():
            bucket[val].append(key)
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return(res)