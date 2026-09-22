class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        t_freq = Counter(t)
        l,r = 0,0
        resLen = float('inf')
        res = ''
        s_freq = {}
        have,req = 0,len(t_freq)
        while r<len(s):
            s_freq[s[r]] = s_freq.get(s[r],0)+1
            if s[r] in t_freq and t_freq[s[r]] == s_freq[s[r]]:
                have+=1
            while have == req:
                if (r-l+1)<resLen:
                    resLen = (r-l+1)
                    res = s[l:r+1]
                if s[l] in t_freq and t_freq[s[l]] == s_freq[s[l]]:
                    have-=1
                s_freq[s[l]]-=1
                l+=1
            r+=1
        return res if resLen!=float('inf') else ''