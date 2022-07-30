# d={}
# @lru_cache(None)
def f(index,amount,d,coins):

            if index==0:
                if amount%coins[index]==0:
                    return amount//coins[index]
                else:
                    return 999999
            if (index,amount) in d:
                return d[(index,amount)]
            
            n1=f(index-1,amount,d,coins)
            n2=999999
            if coins[index]<=amount:
                n2=1+f(index,amount-coins[index],d,coins)
            d[(index,amount)]=min(n1,n2)
            return d[(index,amount)]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d={}
        # d = [[9999 for i in range(amount+1000) for j in range(amount+1000)]]
        n=len(coins)
        # d = [[999999 for i in range(index+1)] for j in range(amount+1)]
        m=f(n-1,amount,d,coins)
        if m==999999:
            return -1
        return m
            
        