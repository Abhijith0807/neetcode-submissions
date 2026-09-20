class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashdict=dict()
        for i in nums:
            if i not in hashdict:
                hashdict[i]=1
            else:
                hashdict[i]+=1
        bucket= [[] for i in range(len(nums) + 1)]
        for val,cnt in hashdict.items():
            bucket[cnt].append(val)
        result=[]
        for j in range(len(bucket)-1,0,-1):
            for n in bucket[j]:
                result.append(n)
                if len(result)==k:
                    return(result)


        
        