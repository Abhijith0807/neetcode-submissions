class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap=dict()
        res=0
        lptr=0
        for rptr in range(len(s)):
            hashMap[s[rptr]]=1+hashMap.get(s[rptr],0)
            while (rptr-lptr+1)-max(hashMap.values())>k:
                hashMap[s[lptr]]-=1
                lptr+=1
            res=max(res,rptr-lptr+1)
        return(res)


        