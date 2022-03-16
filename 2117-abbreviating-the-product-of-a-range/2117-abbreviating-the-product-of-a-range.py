class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        k=1
        for i in range(left,right+1):
            k*=i
        l=str(k)
        k=str(l)
        len_0=0
        if l[-1]=='0':
            len_0=0
            rem=''
            for i in k[::-1]:
                if i=='0':
                    len_0+=1
                else:
                    break
            rem=str(int(k[::-1]))
            if len(str(rem))>10:
                k=rem[::-1][:5]+'...'+rem[::-1][-5:]
            else:
                n=int(k[::-1])
                n=str(n)[::-1]
                k=n
        k+='e'
        k+=str(len_0)
        return k
            
            
                    
            
            
        