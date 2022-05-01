def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        r=len(set(candyType))
        if n>r:
            return r
        else:
            return n