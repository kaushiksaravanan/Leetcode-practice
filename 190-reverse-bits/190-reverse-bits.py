class Solution:
    def reverseBits(self, n: int) -> int:
        a=[]
        while(n>0):
            a.append(n%2)
            n=n//2
        for i in range(32-len(a)):
            a.append(0)
        print("".join([str(i) for i in a]))
        return int("".join([str(i) for i in a]),2)
        