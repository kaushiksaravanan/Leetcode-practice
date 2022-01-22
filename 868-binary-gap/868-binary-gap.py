class Solution:
    def binaryGap(self, n: int) -> int:
        k=0
        c=0
        for i in bin(n).replace("0b",""):
            if i=='1':
                if k<c:
                    k=c
                c=0
            c+=1    
        return k