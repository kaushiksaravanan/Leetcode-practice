class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        print(bin(l),bin(r))

        x=0
        c=0
        while l!=r:   
            r=r>>1
            l=l>>1
            c+=1
            # break
        print(bin(l),bin(r))
        return r<<c