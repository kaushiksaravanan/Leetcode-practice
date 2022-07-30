class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        t=a|b
        print(t)
        
        n0=bin(a)[2:][::-1]
        n1=bin(b)[2:][::-1]
        n2=bin(c)[2:][::-1]
        n=[len(n0),len(n1),len(n2)]
        max_l=max(n)
        ind=0
        for i in n:
            if ind==0:
                if i!=max_l:
                    for _ in range(max_l-n[ind]):
                        n0+='0'
            if ind==1:
                if i!=max_l:
                    for _ in range(max_l-n[ind]):
                        n1+='0'
            if ind==2:
                if i!=max_l:
                    for _ in range(max_l-n[ind]):
                        n2+='0'
            ind+=1
        l=0
        c=0
        print(n0,n1,n2)
        for i in range(len(n2)):
            if n0[i]=='1' and n1[i]=='1' and n2[i]=='0':
                c+=2
            if n0[i]=='1' and n1[i]=='0' and n2[i]=='0':
                c+=1
            if n0[i]=='0' and n1[i]=='1' and n2[i]=='0':
                c+=1
            if n0[i]=='0' and n1[i]=='0' and n2[i]=='1':
                c+=1
        return c
            