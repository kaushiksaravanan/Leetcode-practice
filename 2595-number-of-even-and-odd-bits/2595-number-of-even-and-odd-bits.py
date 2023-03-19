class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n=bin(n).replace('0b','')
        print(n)
        m=0
        l=0
        e=o=0
        for i in n[::-1]:
            if i=='1':
                if l%2==0:
                    e+=1
                else:
                    o+=1
            l+=1
            # if 
        return [e,o]