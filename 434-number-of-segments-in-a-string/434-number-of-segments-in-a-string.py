class Solution:
    def countSegments(self, s: str) -> int:
        
        s=s.strip(" ")
        if len(s)==0:
            return 0
        if s=="":
            return 0
        k=0
        for i in s.split(" "):
            if i.strip(" ")=="":
                pass
            else:
                print(i.strip(" "),end='+++')
                print()
                k+=1
        print('ffffffffff')
        return k
        