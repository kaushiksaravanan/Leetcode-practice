class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        r=len(set(candyType))
        if n>r:
            return r
        return n