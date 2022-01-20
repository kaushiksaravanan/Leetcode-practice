class Solution:
    def divisorGame(self, n: int) -> bool:
        x=1
        k=0
        while n%x==0 and 0<x<n:
            n=n-x
            k+=1
        if k%2==0:
            return False
        return True
        
            
        