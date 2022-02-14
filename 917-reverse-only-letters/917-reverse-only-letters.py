class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        first=0
        end=len(s)-1
        while(end>first):
            print(s[first],s[end])
            if s[first].isalpha() and s[end].isalpha():
                t=s[first]
                s[first]=s[end]
                s[end]=t
                first+=1
                end-=1
                continue
            elif not(s[end].isalpha()):
                end-=1
            elif not(s[first].isalpha()):
                first+=1
        return "".join(s)
            
                
                
        