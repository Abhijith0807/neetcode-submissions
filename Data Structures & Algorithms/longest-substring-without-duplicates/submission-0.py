class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rptr=0
        q=deque()
        maxlen=0
        for lptr in range(len(s)):
            while rptr<len(s):
                if s[rptr] not in q:
                    q.append(s[rptr])
                    maxlen=max(maxlen,len(q))
                    rptr+=1
                else:
                    q.popleft()
                    break
        return(maxlen)


        