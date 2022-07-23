
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        temp=[0]*100000
        def f(n):
            if temp[n]!=0:
                return temp[n]
            if n>(len(cost)-1):
                return 0
            n1=f(n+1)+cost[n]
            n2=f(n+2)+cost[n]
            # n3=f(n+1)
            temp[n]=min(n1,n2)
            return temp[n]
        return min(f(0),f(1))
            
        
        