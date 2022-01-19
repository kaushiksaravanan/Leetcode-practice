class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        ke=[]
        for i in range(0,n,k):
                ke.append(s[i:i+k])
        if len(ke)>=2:
            if len(ke[-1])!=len(ke[-2]):
                for i in range(len(ke[-2])-len(ke[-1])):
                    ke[-1]+=fill
        if len(s)<k:
            for i in range(k-len(s)):
                ke[-1]+=fill
        return ke
                
        