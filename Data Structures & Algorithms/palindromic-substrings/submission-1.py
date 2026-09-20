class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            lptr,rptr=i,i
            while lptr>=0 and rptr<len(s) and s[lptr]==s[rptr]:
                count+=1
                lptr-=1
                rptr+=1
            lptr,rptr=i,i+1
            while lptr>=0 and rptr<len(s) and s[lptr]==s[rptr]:
                count+=1
                lptr-=1
                rptr+=1
        return(count)