class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashdict=dict()
        for i in s:
            if i in hashdict:
                hashdict[i]=hashdict[i]+1
            else:
                hashdict[i]=1
        for i in t:
            if i in hashdict:
                hashdict[i]=hashdict[i]-1
            else:
                return(False)
        for i in hashdict.keys():
            if hashdict[i]!=0:
                return(False)
        return(True)