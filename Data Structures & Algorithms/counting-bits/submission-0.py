class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0 for i in range(n+1)]
        curr=1
        offset=1
        while curr<=n:
            if offset*2==curr:
                offset=curr
            dp[curr]=1+dp[curr-offset]
            curr+=1
        return(dp)
