class Solution:
    def reverseBits(self, n: int) -> int:
        res=[0]*32
        curr=0
        while n:
            res[curr]=n%2
            n=n//2
            curr+=1
        offset=31
        sum=0
        for i in res:
            sum=sum+i*(2**offset)
            offset-=1
        return(sum)