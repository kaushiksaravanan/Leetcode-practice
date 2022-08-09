class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=-99999
        min_price=999999
        for i in range(len(prices)):
            min_price=min(prices[i],min_price)
            profit=max(profit,prices[i]-min_price) 
        return profit
        