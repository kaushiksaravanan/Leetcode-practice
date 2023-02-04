class Solution:
    def convertToTitle(self, c: int) -> str:
        ans=''
        apl='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while c>0:
            c-=1
            n=c%26
            print(n)
            
            ans+=apl[n]
            c=c//26
            # if c%26==0:
            #     c=(c//26)-1
        return ans[::-1]