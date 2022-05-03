class Solution:
    def digitSum(self, s: str, k: int) -> str:
        m=[]
        while len(s)>k:
            m=[]
            for i in range(0,len(s),k):
                m.append(s[i:i+k])
            ke=[]
            for i in m:
                z=0
                for j in i:
                    z+=int(j)
                ke.append(str(z))
            s=''.join(ke)
            del m
            m=ke
            if len(s)<=k:
                break
        return s

            
        