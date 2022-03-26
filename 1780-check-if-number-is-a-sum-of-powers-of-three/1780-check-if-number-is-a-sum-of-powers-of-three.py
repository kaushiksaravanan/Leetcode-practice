class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i=int(math.log(n,3))
        k=[]
        while n>0 and i>=0:
            if (n-(3**i))>=0:
                n-=(3**i)
                k.append(i)
            i-=1
        print(k)
        print(n)
        return n==0
            
        