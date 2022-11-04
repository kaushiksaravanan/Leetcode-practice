class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiop"
        a+=a.upper()
        b="asdfghjkl"
        b+=b.upper()
        c="zxcvbnm"
        c+=c.upper()

        x=[]
        for i in words:
            
            a1=0
            a2=0
            a3=0
            for j in i:
                if j in a:
                    a1+=1
                if j in b:
                    a2+=1
                if j in c:
                    a3+=1
            print(a1,a2,a3)
            if a1+a2+a3==a1 or a1+a2+a3==a2 or a1+a2+a3==a3:
                x.append(i)
        return x