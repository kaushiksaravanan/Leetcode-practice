class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        e=[]
        for i in range(0,len(s),k):
            e.append(s[i:i+k])
        l=[]
        print(e)
        k=0
        for i in e:
            if k%2==0:
                l.append(i[::-1])
            else:
                l.append(i)
            k+=1
        return "".join(l)
            
            