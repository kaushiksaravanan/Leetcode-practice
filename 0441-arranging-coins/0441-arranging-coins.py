class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n<=2:
            return 1
        for i in range(n):
            if (i*(i+1))//2>n:
                return i-1
            if (i*(i+1))//2==n:
                return i