class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        buyDay=0
        for sellDay in range(1,len(prices)):
            currProfit=prices[sellDay]-prices[buyDay]
            if currProfit<0:
                buyDay=sellDay
            else:
                maxProfit=max(maxProfit,currProfit)
        return(maxProfit)

        