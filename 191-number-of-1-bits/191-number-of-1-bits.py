class Solution:
    def hammingWeight(self, n: int) -> int:
        k=bin(n)[2:]
        print(k)
        c=0
        for i in k:
            if i=='1':
                c+=1
        return c
        