class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        c=0
        while l!=r:   
            r=r>>1
            l=l>>1
            c+=1
        return r<<c