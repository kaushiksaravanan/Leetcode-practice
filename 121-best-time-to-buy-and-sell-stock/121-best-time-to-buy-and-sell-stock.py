class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=-99999
        min_price=999999
        for i in prices:
            min_price=min(i,min_price)
            profit=max(profit,i-min_price) 
        return profit
        