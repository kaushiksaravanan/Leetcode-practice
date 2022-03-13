class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for i in s:
            if i=='#' and len(s1)!=0:
                s1.pop()
            else:
                s1.append(i)
        for i in t:
            if i=='#' and len(s2)!=0:
                s2.pop()
            else:
                s2.append(i)
        # print(s1,s2)
        try:
            s1.remove('#')
        except:
            pass
        try:
            s2.remove('#')
        except:
            pass
        print(s1,s2)

        return s1==s2
                
        
        