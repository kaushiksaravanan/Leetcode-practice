class Solution:
    def countBits(self, n: int) -> List[int]:
        k=[]
        while n>=0:
            k.append(bin(n).count('1'))
            n-=1
        print(k)
        return k[::-1]
        