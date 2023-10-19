class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        k1=[]
        k2=[]
        for i in s:
            if i=='#':
                if k1:
                    k1.pop()
            else:
                k1.append(i)
        
        for i in t:
            if i=='#':
                if k2:
                    k2.pop()
            else:
                k2.append(i)
        return k1==k2
        