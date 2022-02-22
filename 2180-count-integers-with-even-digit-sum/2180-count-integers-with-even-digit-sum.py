class Solution:
    def countEven(self, num: int) -> int:
        c=0
        while(num>0):
            if sum([int(i) for i in list(str(num))])%2==0:
                c+=1
            num-=1
        return c
        