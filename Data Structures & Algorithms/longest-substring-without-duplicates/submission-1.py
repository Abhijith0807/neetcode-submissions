class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lptr=0
        res=0
        substr=deque()
        for rptr in range(len(s)):
            if s[rptr] not in substr:
                substr.append(s[rptr])
                res=max(res,rptr-lptr+1)
            else:
                while substr:
                    popval=substr.popleft()
                    lptr+=1
                    if s[rptr] not in substr:
                        substr.append(s[rptr])
                        res=max(res,rptr-lptr+1)
                        break
        return(res)