class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPtr = prices[0]
        profit = 0
        
        for x in prices:
            if x < buyPtr:
                buyPtr = x
                
            if x - buyPtr > profit:
                profit = x - buyPtr
                
        return profit