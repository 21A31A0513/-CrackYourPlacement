class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        else:
            profit=0
            m=prices[0]
            for i in range(1,len(prices)):
                profit=max(profit,prices[i]-m)
                m=min(m,prices[i])
            return profit
