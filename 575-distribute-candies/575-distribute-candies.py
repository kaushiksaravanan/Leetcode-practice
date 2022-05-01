class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d={}
        n=0
        for i in candyType:
            d[i]=1
            n+=1
        r=len(d)
        n=n//2
        if n>r:
            return r
        return n