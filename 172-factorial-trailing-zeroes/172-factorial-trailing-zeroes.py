class Solution:
    def trailingZeroes(self, n: int) -> int:
        k=1
        x=0
        while(int(math.floor(n/5**k))!=0):
            x+=int(math.floor(n/5**k))
            k+=1
        return x
        