
        
class Solution:
    def numDecodings(self, s: str) -> int:
        alp='abcdefghijklmnopqrstuvwxyz'
        d={}
        l=1
        for i in alp:
                    d[str(l)]=1
                    l+=1    
        # print(d)
        @cache
        def rec(chr):
            k=0
            if chr in d and len(chr)!=1:
                k+=1
            if chr[0]=='0':
                return k
            if len(chr)==1 and chr!='0':
                return k+1
            else:
                n=len(chr)
                for i in range(1,n):
                    n1=chr[:i]
                    if len(n1)==0:
                        continue

                    if int(n1)<=26:
                        k1=rec(chr[i:])
                        k+=k1
                    else:
                        break
                        pass
                return k
        return rec(s)
                
            

        
        