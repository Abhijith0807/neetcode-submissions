class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist=list()
        for i in s:
            if i.isalnum():
                slist.append(i)
        s=''.join(slist)
        s=s.upper()
        lptr=0
        rptr=len(s)-1
        while lptr<=rptr:
            if s[lptr]!=s[rptr]:
                    return(False)
            else:
                lptr+=1
                rptr-=1
        return(True)
        