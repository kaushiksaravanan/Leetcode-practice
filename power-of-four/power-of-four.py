import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0:
            return 4**int(math.log(n,4))==n
        if n<0:
            t=n
            n=-t
            if int(math.log(n,4))%2==1:
                return 4**int(math.log(n,4))==-n
                
                
        
        