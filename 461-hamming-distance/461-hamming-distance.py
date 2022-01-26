class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=bin(x).replace("0b","")
        b=bin(y).replace("0b","")
        a_l=len(a)
        b_l=len(b)
        print(a,b,len(a),len(b))
        max_l=max(a_l,b_l)
        min_l=min(a_l,b_l)
        
        a=a.replace(a[0],((max_l-a_l)*"0")+a[0],1)
        b=b.replace(b[0],((max_l-b_l)*"0")+b[0],1)
        k=0
        print(a,b,len(a),len(b))
        for i in range(max_l):
            if a[i]!=b[i]:
                k+=1
        return k
        

        