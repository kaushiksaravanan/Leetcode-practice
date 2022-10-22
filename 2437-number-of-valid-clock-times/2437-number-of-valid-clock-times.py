class Solution:
    def countTime(self, time: str) -> int:
        k=time.split(":")
        h=k[0]
        m=k[1]
        n1=1
        if h[0]=='?':
            if h[1]!='?':
                if int(h[1])<=3:
                    n1*=3
                if int(h[1])>3:
                    n1*=2
            else:
                n1+=23
        if h[1]=='?' and h[0]!='?' and h[0]!='2':
            n1*=10
        if h[1]=='?' and h[0]!='?' and h[0]=='2':
            n1*=4
        
        print(n1)
        if m[0]=='?' and m[1]!='?':

            n1*=6
        if m[1]=='?' and m[0]!='?':
            n1*=10
        if m[1]=='?' and m[0]=='?':
            n1*=60
        return n1
                
            