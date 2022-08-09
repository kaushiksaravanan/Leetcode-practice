class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_price=prices[0]
        for i in prices:
            min_price=min(i,min_price)
            profit=max(profit,i-min_price) 
        return profit
        